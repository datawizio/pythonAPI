"""
running tests for all test_*.py files in curr dir

Yuo must specify runTest function for all those tests

"""
import imp
import os
import unittest


def run():

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(curr_dir)
    files.pop(files.index('__init__.py'))
    for file in files:
        file_path = os.path.join(curr_dir, file)
        if os.path.isfile(file_path) and os.path.splitext(file)[1] == '.py' and file.startswith('test_'):
            test = imp.load_source(file, os.path.join(curr_dir, file))
            suite = unittest.TestLoader().loadTestsFromModule(test)
            unittest.TextTestRunner().run(suite)