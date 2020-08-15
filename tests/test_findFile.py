import unittest
import os
import shutil
import find_file


class TestFindFile(unittest.TestCase):
    def setUp(self):
        os.makedirs('/tmp/dir1/dir2/dir3')
        os.mkdir('/tmp/dir1.5')
        fhand1 = open('/tmp/dir1/1.txt', 'w+')
        fhand2 = open('/tmp/dir1/dir2/1.txt', 'w+')
        fhand1.close()
        fhand2.close()

    def tearDown(self):
        shutil.rmtree('/tmp/dir1')
        shutil.rmtree('/tmp/dir1.5')

    def test_findFile(self):
        fileOccurences1 = find_file.findFile('/tmp', '1.txt', recursive=True)
        self.assertEqual(fileOccurences1, ['/tmp/dir1/dir2/1.txt', '/tmp/dir1/1.txt'])

        fileOccurences2 = find_file.findFile('/tmp', '1.txt')
        self.assertEqual(fileOccurences2, [])

        fileOccurences3 = find_file.findFile('/tmp/dir1', '1.txt')
        self.assertEqual(fileOccurences3, ['/tmp/dir1/1.txt'])

        fileOccurences4 = find_file.findFile('/tmp', 'foo.txt')
        self.assertEqual(fileOccurences4, [])




