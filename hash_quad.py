class HashTable:

    def __init__(self, table_size=191):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    '''def __repr__(self):
        return str(self.hash_table)'''

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        idx = (self.horner_hash(key))
        n = 0
        while self.hash_table[(idx + n**2)%self.table_size] is not None:
            if self.hash_table[(idx + n**2)%self.table_size][0] == key:
                self.num_items -=1
                break
            n += 1
        self.hash_table[(idx+n**2)%self.table_size] = (key,value)


        self.num_items += 1

        if self.get_load_factor() > 0.5:
            self.table_size = (self.table_size*2) + 1
            temp = self.hash_table
            self.hash_table = [None]*self.table_size
            self.num_items = 0

            for tup in temp:
                if tup is not None:
                    self.insert(tup[0],tup[1])

            
            '''for val in temp:
                idx = self.horner_hash(val[0])
                n = 0
                while self.hash_table[(idx + n**2)%self.table_size] is not None:
                    n += 1
                self.hash_table[(idx+n**2)%self.table_size] = (val[0],val[1])'''

        

    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        #key = key.lower()
        n = min(len(key),8)
        summation = 0
        for i in range(n):
            summation += (ord(str(key[i]))*(31**(n-1-i)))
        return summation%self.table_size


    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        
        idx = self.get_index(key)
        if idx is None:
            return False
        return True


        '''index = self.horner_hash(key)
        temp = index
        n = 1
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return True
            elif self.hash_table[index][0] != key:
                index = (temp + (n ** 2)) % self.table_size
                n += 1
        return False'''

        '''idx = (self.horner_hash(key))
        n = 0
        while self.hash_table[(idx + n**2)%self.table_size] is not None:
            if self.hash_table[(idx + n**2)%self.table_size][0] == key:
                return True
        return False


        tester = self.get_all_keys()
        for val in tester:
            if val == key:
                return True
        return False'''

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        
        idx = self.horner_hash(key)
        n = 0
        while self.hash_table[(idx + n**2)%self.table_size] is not None:
            if self.hash_table[(idx + n**2)%self.table_size][0] == key:
                return (idx + n**2)%self.table_size
            n += 1
        return None



        '''if self.in_table(key) == False:
            return None
        idx = (self.horner_hash(key))
        n = 0
        while self.hash_table[(idx + n**2)%self.table_size][0] != key:
            n += 1

        return (idx+n**2)%self.table_size'''

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        final = []
        for val in self.hash_table:
            if val is not None:
                final.append(val[0])
        return final

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        
        idx = self.get_index(key)
        if idx is None:
            return None
        return self.hash_table[idx][1]


        '''if self.in_table(key) == False:
            return None
        
        idx = (self.horner_hash(key))
        n = 0
        while self.hash_table[(idx + n**2)%self.table_size][0] != key:
            n += 1

        return self.hash_table[(idx+n**2)%self.table_size][1]'''

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items/self.table_size
