
"""Tests debug file"""
import logging


class DebugTest(logs):
    def test_debug_file(self):
        self.assertLogs(self, logging.DEBUG)


"""Tests request log file is created"""
