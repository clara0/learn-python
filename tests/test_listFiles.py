import unittest
import os
import shutil
import list_files


class TestListFiles(unittest.TestCase):
    def setUp(self):
        os.makedirs('/tmp/a/b/c')
        os.mkdir('/tmp/a/aa')
        with open('/tmp/a/under_a.txt', 'w+') as fhand1:
            pass
        with open('/tmp/a/b/under_b.txt', 'w+') as fhand2:
            pass
        with open('/tmp/a/b/c/under_c.txt', 'w+') as fhand3:
            pass

    def tearDown(self):
        shutil.rmtree('/tmp/a')

    def test_listFiles(self):
        listedContents = list_files.listFiles('/tmp/a', [], recursive=True)
        self.assertEqual(listedContents, [['aa'], 'under_a.txt', ['b', 'under_b.txt', ['c', 'under_c.txt']]])

        listedContents = list_files.listFiles('/tmp/a', [], recursive=False)
        self.assertEqual(listedContents, ['aa', 'under_a.txt', 'b'])

        listedContents = list_files.listFiles('/tmp/a', [])
        self.assertEqual(listedContents, ['aa', 'under_a.txt', 'b'])

