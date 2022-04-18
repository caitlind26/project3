
"""Tests debug file"""
import logging
import unittest

import logs
class DebugTest(unittest.TestCase):
    def test_debug_file(self):
        self.assertLogs(self, logging.DEBUG)

"""Tests request log file is created"""
