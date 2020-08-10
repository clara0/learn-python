import unittest
import os
import copy_file


class TestCopyFiles(unittest.TestCase):
    def test_copyFile(self):
        source = '/Users/clara/PycharmProjects/learn-python/date_and_time.py'
        destination = '/Users/clara/PycharmProjects/learn-python/a.txt'
        overwrite = True
        fileExists = False
        copy_file.copyFile(source, overwrite, fileExists, destination)
        sourceSize = os.stat('/Users/clara/PycharmProjects/learn-python/date_and_time.py')
        destSize = os.stat('/Users/clara/PycharmProjects/learn-python/a.txt')
        self.assertEqual(sourceSize.st_size, destSize.st_size)

        source = '/Users/clara/PycharmProjects/learn-python/date_and_time.py'
        destination = '/Users/clara/PycharmProjects/learn-python/a.txt'
        overwrite = False
        fileExists = False
        copy_file.copyFile(source, overwrite, fileExists, destination)
        sourceSize = os.stat('/Users/clara/PycharmProjects/learn-python/date_and_time.py')
        destSize = os.stat('/Users/clara/PycharmProjects/learn-python/a.txt')
        self.assertEqual(sourceSize.st_size, destSize.st_size)