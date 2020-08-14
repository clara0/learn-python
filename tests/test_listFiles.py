import unittest
import os
import shutil
import list_files


class TestListFiles(unittest.TestCase):
    def setUp(self):
        os.makedirs('/tmp/a/b/c')
        os.mkdir('/tmp/a/aa')
        fhand1 = open('/tmp/a/under_a.txt', 'w+')
        fhand2 = open('/tmp/a/b/under_b.txt', 'w+')
        fhand1.close()
        fhand2.close()

    def tearDown(self):
        shutil.rmtree('/tmp/a')

    def test_listFiles(self):
        listedContents = list_files.listFiles('/tmp/a', [], recursive=True)
        self.assertEqual(listedContents, [['aa'], 'under_a.txt', ['b', 'under_b.txt', 'c']])

        listedContents = list_files.listFiles('/tmp/a', [], recursive=False)
        self.assertEqual(listedContents, ['aa', 'under_a.txt', 'b'])

        listedContents = list_files.listFiles('/tmp/a', [])
        self.assertEqual(listedContents, ['aa', 'under_a.txt', 'b'])

