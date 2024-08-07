class HashTable:
    def __init__(self, max=10):
        self.table = [[] for _ in range(max)]
        self.max = max
        self.count = 0 #length
        
    def _hash(self,key):
        return hash(key) % self.max # compute the hash value => location in the hash
    
    def __len__(self):
        return self.count
    
    def __str__(self):
        return str(self.table)
    
    def insert(self, key, value):
        index = self._hash(key)
        for i in self.table[index]:
            if i[0] == key:
                i[1] = value # update value if key existed
                return
        self.table[index].append([key,value])
        self.count+=1
        
    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[i] = []
                self.count -= 1
                return
            else:
                raise KeyError(f"{key} does not exist in hash table")
            
    def exists(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                return True
            else:
                return False
            
    
        