import os
import sys
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
import time
import random
import hashlib
import string
import json
import shutil
from . import contants
from . import util

KEY_LENGTH = 32

TAMPER_ALERT_RESULT = {
    "score": 0,
    "output": "Result tampering detected!",
    "visibility": "visible",
    "extra_data": {}
}


class ResultWatchdog:
    def __init__(self, result_file, timeout=600):
        self.hash_file = "./result_hash.txt"
        self.tamper_file = "./tamper.json"
        self.key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=KEY_LENGTH))
        self.result_file = result_file
        self.timeout = timeout
        self.tamper_alert_result = json.dumps(TAMPER_ALERT_RESULT)
        self.tamper_hash = self._generate_hash(self.tamper_alert_result)

    def launch(self):
        if contants.IS_WINDOWS:
            print("Result Watchdog is not available on Windows")
            return
        if os.fork() != 0: return
        self._launch_watchdog()

    def _launch_watchdog(self):
        path = os.path.abspath(os.path.dirname(self.result_file))
        print(path)
        event_handler = Handler(self.result_file, lambda: self._validate_result())
        observer = Observer()
        observer.schedule(event_handler, path=path, recursive=False)
        observer.start()
        start = time.time()
        while time.time() - start < self.timeout:
            time.sleep(1)
        observer.stop()
        observer.join()
        print("Watchdog terminated")
        sys.exit()
        

    def _generate_hash(self, s):
        h = hashlib.sha256()
        h.update(s.encode('utf-8'))
        h.update(self.key.encode("utf-8"))
        return h.hexdigest()

    def submit_hash(self, s):
        with open(self.hash_file, "w+") as f:
            f.write(self._generate_hash(s))

    def _validate_result(self):
        if not os.path.exists(self.hash_file):
            self._write_tamper_alert_result()
            return
        
        with open(self.hash_file) as f:
            ref_hash = f.read()

        with open(self.result_file) as f:
            result = f.read()
        result_hash = self._generate_hash(result)
        if result_hash != ref_hash:
            self._write_tamper_alert_result()

    def _write_tamper_alert_result(self):
        os.remove(self.result_file)
        with open(self.hash_file, "w+") as f:
            f.write(self.tamper_hash)
        
        succeeded = False
        while not succeeded:
            try:
                with open(self.result_file, "w+") as f:
                    f.write(self.tamper_alert_result)
                succeeded = True
            except PermissionError:
                pass

class Handler(PatternMatchingEventHandler):
    def __init__(self, result_file, callback):
        # print(os.path.basename(result_file))
        PatternMatchingEventHandler.__init__(self, patterns=['*.json'], ignore_directories=True, case_sensitive=False)
        self.callback = callback

    def on_created(self, event):
        self.callback()

    def on_modified(self, event):
        self.callback()
