from HashTable import HashTable
class TestHashTable:
    def initialize(hashTable: HashTable):
        hashTable.insert(5,6)
        hashTable.insert(6,8)
        hashTable.insert(7,9)
        hashTable.insert(4,3)
        print(f"The new hash table is: {hashTable}")
        
    def testDelete(hashTable: HashTable, key):
        hashTable.delete(key)
        print(f"The new hash table is: {hashTable}")
        
    def testExists(hashTable: HashTable, key):
        if hashTable.exists(key) == True:
            print(f"The new hash table is: {hashTable}")
        else:
            print(f"the key does not exist")
            
def main():
    table = HashTable(10)
    TestHashTable.initialize(table)
    TestHashTable.testDelete(table,4)
    TestHashTable.testExists(table,4)
            
if __name__ == "__main__":
        
    main()

