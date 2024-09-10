from MaxHeap import MaxHeap
class TestHeapMax:
    def initialization(m:MaxHeap):
        m.insert(5)
        m.insert(6)
        m.insert(9)
        m.insert(10)
        m.insert(22)
        m.insert(15)
        m.insert(26)
        m.insert(4)

    def test_is_empty(m:MaxHeap):
        if m.is_empty() == True:
            print("The heap is empty")
        print("The heap is not empty")

    def test_get_max(m:MaxHeap):
        if m.is_empty() == True:
            print("The heap is empty")
        else:
            print(f"The maximum value of the heap is: {m.get_max}")

    def test_print(m:MaxHeap):
        if m.is_empty() == True:
            print("The heap is empty")
        else:
            print(f"The heap is: {m}")

if __name__ == "__main__":
    m = MaxHeap()
    TestHeapMax.initialization(m)
    TestHeapMax.test_is_empty(m)
    TestHeapMax.test_print(m)