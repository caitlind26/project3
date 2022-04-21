import os
from app import logs

"""Tests debug file"""
def test_debug_file():
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../debug')
    assert os.path.exists(logdir) == True

"""Tests request log file is created"""
def test_request_log_file():
    assert 'request.log' in logs