"""
 filename: test_code.py
 Author: Teressia Muriruri
"""
import unittest

from code import check_files


class TestFilesChecking(unittest.TestCase):
    """test whether files get checked successfully"""

    def setUp(self):
        self.file_checker = check_files()

    def test_file_checking_success(self):
        """returns True """
        self.assertEqual(True, self.file_checker)
