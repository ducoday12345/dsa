from BinarySearch import BinarySearch
class TestBinarySearch:
    def initialization(self, arr: list):
        self.arr = BinarySearch(arr)


    def test_iterative(self,target):
        print(f"index of {target} in {self.arr.BinarySearch(target)}")

    def test_recursive(self,target):
        print(f"index of {target} in {self.arr.BinarySearchRecursive(target)}")

def main():
    lis = TestBinarySearch()
    lis.initialization([1,2,3,3,4,6,8,9,10])
    lis.test_iterative(7)
    lis.test_recursive(7)

if __name__ == "__main__":
    main()