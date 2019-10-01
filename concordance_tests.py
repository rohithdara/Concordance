import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

    def test_errors(self):
        con = Concordance()
        with self.assertRaises(FileNotFoundError):
            con.load_stop_table('wrong.txt')

        with self.assertRaises(FileNotFoundError):
            con.load_concordance_table('wrong.txt')

    def test_special_words(self):
        con = Concordance()
        con.load_stop_table('stop_words.txt')
        con.load_concordance_table('tester.txt')
        con.write_concordance('tester_con.txt')
        self.assertTrue(filecmp.cmp('tester_con.txt','tester_out.txt'))

    def test_empty_file(self):
        con = Concordance()
        con.load_stop_table('stop_words.txt')
        con.load_concordance_table('empty_file.txt')
        con.write_concordance('empty_file_out.txt')
        self.assertTrue(filecmp.cmp('empty_file_out.txt','empty_file_sol.txt'))

    def test_single_word(self):
        con = Concordance()
        con.load_stop_table('stop_words.txt')
        con.load_concordance_table('single_word.txt')
        con.write_concordance('single_word_out.txt')
        self.assertTrue(filecmp.cmp('single_word_out.txt','single_word_sol.txt'))





if __name__ == '__main__':
   unittest.main()
