"""Manage export proceses."""

import threading
import time
import json
import sys

import hrflow as hf

from .profile_retriever import ProfileRetriever
from .worker import Worker
from .printer import Printer


class Supervisor(object):
    """Class that manage export process."""

    def __init__(self, client, source_ids, target, v_level, n_worker=3, logfile=None):
        """Init."""
        self.client = client
        self.n_worker = n_worker
        self.workers = {}
        self.lock_worker = threading.Lock()

        self.source_ids = source_ids
        # number of source at start (to calc advancement percentagages.)
        self.n_start_sources = len(self.source_ids)
        self.current_source = ""

        # target file
        self.target = target
        # verbose level
        self.v_level = v_level
        self.logfile = None
        if logfile is not None:
            self.logfile = logfile

        self.p_retriever = ProfileRetriever(self.client, self.source_ids)
        self.profiles_to_export = []

        # these variable will be reset when a source starts
        # number of profile at start (for a source) (to calc advancement percentagages.)
        self.n_start_profiles_to_export = 0
        self.n_profile_with_fail = 0
        self.export_result = []

        self.n_global_exported_profile = 0
        self.n_global_profile_with_fail = 0
        self.log_printer = Printer(self)

    def _set_worker_profile(self, workerID):
        if len(self.profiles_to_export) == 0:
            return
        self.workers[workerID].set_profile(self.profiles_to_export.pop(), self.worker_callback)

    def _init_workers(self):
        for i in range(self.n_worker):
            self.workers[i] = Worker(i, self.client, self.target)
            # Give a file before start a worker to avoid the workers to die instantly
            self._set_worker_profile(i)

    def worker_callback(self, workerID, result):
        """Call when a worker has finished to process a profile."""
        # locked to avoid data race beetwen worker
        self.lock_worker.acquire()
        self.export_result.append(result)
        if not result.is_success:
            self.n_profile_with_fail += 1
            self.n_global_profile_with_fail += 1
        self.n_global_exported_profile += 1
        self._set_worker_profile(workerID)

        self.log_printer.print_update(result)
        self.lock_worker.release()

    def _process_a_source(self):
        self.n_start_profiles_to_export = len(self.profiles_to_export)
        self.n_profile_with_fail = 0
        self.export_result = []
        self._init_workers()
        self.lock_worker.acquire()
        self.log_printer.print_update(None)
        for idx, w in enumerate(self.workers):
            self.workers[idx].start()
            time.sleep(0.1)
        self.lock_worker.release()
        for idx, w in enumerate(self.workers):
            self.workers[idx].join()
        self.log_printer.print_end_source()

    def _gen_error_source(self, exp):
        data = {
            "err": str(exp)
        }
        return json.dumps(data)

    def start(self):
        """Start export process."""
        self.log_printer.print_start()
        self.profiles_to_export = ['enter the loop la la la!']
        while self.profiles_to_export is not None:
            try:
                self.profiles_to_export, self.current_source = self.p_retriever.get_next_profiles()
                if self.profiles_to_export is not None:
                    self._process_a_source()
            except BaseException as e:
                print("{}".format(self._gen_error_source(e)), file=sys.stderr)

        self.log_printer.print_end()
