import unittest
import os
import copy_file


class TestCopyFiles(unittest.TestCase):
    def setUp(self):
        source = '/tmp/a1.txt'
        self.sourcefile = open(source, 'w+')
        self.sourcefile.write('This is the source file.')
        self.sourcefile.close()

    def tearDown(self):
        source = '/tmp/a1.txt'
        dest = '/tmp/b1.txt'
        os.remove(source)
        os.remove(dest)

    def test_copyFile(self):
        def getFiles():
            sourceFile = '/tmp/a1.txt'
            destFile = '/tmp/b1.txt'
            files = (sourceFile, destFile)
            return files

        files = getFiles()

        overwrite = True
        fileExists = False
        copy_file.copyFile(files[0], overwrite, fileExists, files[1])
        sourceSize = os.stat(files[0])
        destSize = os.stat(files[1])
        self.assertEqual(sourceSize.st_size, destSize.st_size)

        overwrite = False
        fileExists = True
        with self.assertRaises(Exception) as cm:
            copy_file.copyFile(files[0], overwrite, fileExists, files[1])
