from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

        self.stop_table = HashTable(191)
        try:
            fin = open(filename,'r')
        except:
            raise FileNotFoundError

        for line in fin:
            val = line.rstrip('\n')
            self.stop_table.insert(val)

        fin.close()



    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

        self.concordance_table = HashTable(191)
        try:
            fin = open(filename,'r')
        except:
            raise FileNotFoundError

        updater = str.maketrans('','',string.punctuation)

        line_num = 0
        for line in fin:
            line_num+=1
            lst = line.split()
            for word in lst:
                if '-' in word:
                    separated = word.replace('-', ' ').split(' ')
                    for each in separated:
                        if each == '':
                            continue
                        word = each.translate(updater)
                        word = word.lower()
                        if self.stop_table.in_table(word):
                            continue
                        elif not self.num_checker(word):
                            val = self.concordance_table.get_value(word)
                            if val is not None:
                                indiv = val.split()
                                if str(line_num) in indiv:
                                    continue
                                self.concordance_table.insert(word,str(val) + ' ' + str(line_num))
                            elif val is None:
                                self.concordance_table.insert(word,str(line_num))

                elif '-' not in word:
                    word = word.translate(updater)
                    word = word.lower()
                    if word == '':
                        continue
                    if self.stop_table.in_table(word):
                            continue
                    elif not self.num_checker(word):
                        val = self.concordance_table.get_value(word)
                        if val is not None:
                            indiv = val.split()
                            if str(line_num) in indiv:
                                continue
                            self.concordance_table.insert(word,str(val) + ' ' + str(line_num))
                        elif val is None:
                            self.concordance_table.insert(word,str(line_num))

        fin.close()













        '''self.concordance_table = HashTable(191)
        try:
            fin = open(filename,'r')
        except:
            raise FileNotFoundError

        updater = str.maketrans('','',string.punctuation)

        line_num = 0
        for line in fin:
            line_num+=1
            lst = line.split()
            print(line_num)
            for word in lst:
                if '-' in word:
                    separated = word.replace('-', ' ').split(' ')
                    for each in separated:
                        if each == '':
                            continue
                        word = each.translate(updater)
                        word = word.lower()
                        if self.stop_table.in_table(word):
                            continue
                        elif not self.num_checker(word):
                            val = self.concordance_table.get_value(word)
                            if val is not None:
                                if line_num == val[-1]:
                                    continue
                                self.concordance_table.insert(word,val + [line_num])
                            elif val is None:
                                self.concordance_table.insert(word,[line_num])

                elif '-' not in word:
                    word = word.translate(updater)
                    word = word.lower()
                    if word == '':
                        continue
                    if self.stop_table.in_table(word):
                            continue
                    elif not self.num_checker(word):
                        val = self.concordance_table.get_value(word)
                        if val is not None:
                            if line_num == val[-1]:
                                continue
                            self.concordance_table.insert(word,val + [line_num])
                        elif val is None:
                            self.concordance_table.insert(word,[line_num])'''

        '''           
        file = fin.read()
        file = file.replace('-',' ')
        updater = str.maketrans('','',string.punctuation)
        file = file.translate(updater)
        file = file.lower()

        everything = file.splitlines()
        line_num = 0

        
        for line in everything:
            line_num+=1
            lst = line.split()
            for word in lst:
                if self.stop_table.in_table(word):
                    continue
                elif not self.num_checker(word):
                    val = self.concordance_table.get_value(word)
                    if val is not None:
                        if line_num == val[-1]:
                            continue
                        self.concordance_table.insert(word,val + [line_num])
                    elif val is None:
                        self.concordance_table.insert(word,[line_num])

        fin.close()
'''
    def num_checker(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        
        fout = open(filename,'w')

        keys = self.concordance_table.get_all_keys()
        keys.sort()
        key_len = len(keys)
        for key in keys:
            #lines = self.concordance_table.get_value(key)
            #new_lines = map(str,lines)
            fout.write(key + ': ' + self.concordance_table.get_value(key))
            key_len -= 1
            if key_len == 0:
                break
            fout.write('\n')

        fout.close()










'''
        fout = open(filename,'w')

        keys = self.concordance_table.get_all_keys()
        keys.sort()
        key_len = len(keys)
        for key in keys:
            lines = self.concordance_table.get_value(key)
            new_lines = list(map(str,lines))
            fout.write(key + ': ' + ' '.join(new_lines))
            key_len -= 1
            if key_len == 0:
                break
            fout.write('\n')

        fout.close()'''

'''
import time

start = time.time()
con = Concordance()
con.load_stop_table('stop_words.txt')
con.load_concordance_table('empty_file.txt')
con.write_concordance('empty_file_out.txt')
end = time.time()
print(end-start)
'''


