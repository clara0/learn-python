import unittest
import os
import shutil
import find_file


class TestFindFile(unittest.TestCase):
    def setUp(self):
        os.makedirs('/tmp/dir1/dir2/dir3')
        os.mkdir('/tmp/dir1.5')
        with open('/tmp/dir1/1.txt', 'w+') as fhand1:
            pass
        with open('/tmp/dir1/dir2/1.txt', 'w+') as fhand2:
            pass

    def tearDown(self):
        shutil.rmtree('/tmp/dir1')
        shutil.rmtree('/tmp/dir1.5')

    def test_findFile(self):
        fileOccurrences1 = find_file.findFile('/tmp', '1.txt', recursive=True)
        self.assertEqual(fileOccurrences1, ['/tmp/dir1/dir2/1.txt', '/tmp/dir1/1.txt'])

        fileOccurrences2 = find_file.findFile('/tmp', '1.txt')
        self.assertEqual(fileOccurrences2, [])

        fileOccurrences3 = find_file.findFile('/tmp/dir1', '1.txt')
        self.assertEqual(fileOccurrences3, ['/tmp/dir1/1.txt'])

        fileOccurrences4 = find_file.findFile('/tmp', 'foo.txt')
        self.assertEqual(fileOccurrences4, [])




