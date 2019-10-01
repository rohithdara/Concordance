import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)
        self.assertEqual(ht.get_num_items(),1)

    def test_empty_table(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(),0)
        self.assertEqual(ht.get_all_keys(),[])
        self.assertEqual(ht.get_table_size(),7)
        self.assertEqual(ht.get_load_factor(),0)
        self.assertEqual(ht.get_value('adsf'),None)
        self.assertEqual(ht.get_index('asdfdf'),None)

    def test_same_key(self):
        ht = HashTable(10)
        ht.insert('ddd',12)
        self.assertEqual(ht.get_value('ddd'),12)
        ht.insert('ddd',16)
        self.assertEqual(ht.get_value('ddd'),16)

    def test_insert_expand(self):
        ht = HashTable(7)
        ht.insert('lol',134)
        ht.insert('haha',24)
        ht.insert('Djb',66)
        self.assertEqual(ht.get_value('haha'),24)
        self.assertEqual(ht.get_value('lol'),134)
        self.assertEqual(ht.get_index('Djb'),0)
        self.assertEqual(ht.get_index('haha'),2)
        self.assertEqual(ht.get_index('lol'),6)
        self.assertEqual(ht.get_num_items(),3)
        self.assertEqual(ht.get_table_size(),7)
        self.assertAlmostEqual(ht.get_load_factor(),3/7)
        ht.insert('TTT',[1,345,56])
        ht.insert('adfs',(1,2))
        self.assertEqual(ht.get_index('lol'),1)
        self.assertEqual(ht.get_index('Djb'),2)
        self.assertEqual(ht.get_index('TTT'),12)
        self.assertEqual(ht.get_value('adfs'),(1,2))
        self.assertEqual(ht.get_all_keys(),['lol', 'Djb', 'adfs', 'TTT', 'haha'])
        self.assertEqual(ht.get_num_items(),5)
        self.assertEqual(ht.get_table_size(),15)
        self.assertAlmostEqual(ht.get_load_factor(),5/15)
        self.assertEqual(ht.get_value('TTT'),[1,345,56])
        self.assertFalse(ht.in_table('adsfdsfsadfd'))
        self.assertFalse(ht.in_table('asdasdfsadfsdf'))
        self.assertEqual(ht.get_value('Djb'),66)
        self.assertEqual(ht.get_value('lol'),134)
        self.assertEqual(ht.get_value('haha'),24)




if __name__ == '__main__':
   unittest.main()
