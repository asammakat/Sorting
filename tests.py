from sortingAlgorithms import bubbleSort, mergeSort, heapSort
from utils import generateRandomList, isMaxHeap, isSorted, merge
from heap import MaxHeap

def testBubbleSort():
    x = generateRandomList(10000, 1, 10000)
    y = bubbleSort(x)
    if(isSorted(y)):
        print("TEST PASSED -- bubbleSort")
    else:
        print("ERROR: list passed to bubbleSort was not sorted")
    
def testMerge():
    l1 = bubbleSort(generateRandomList(100, 1, 100))
    l2 = bubbleSort(generateRandomList(150, 1, 150))
    result = merge(l1, l2)
    if(isSorted(result)):
        print("TEST PASSED -- merge")
    else:
        print("ERROR: list passed to merge was not sorted")

def testMergeSort():
    x = generateRandomList(1000000, 1, 1000000)
    y = mergeSort(x)
    if(isSorted(y)):
        print("TEST PASSED -- mergeSort")
    else:
        print("ERROR: list passed to mergeSort was not sorted")
    
def testHeapInitialization():
    A = generateRandomList(1000000, 1, 1000000)
    h = MaxHeap(A)
    if(isMaxHeap(h.dump(False))):
        print("TEST PASSED -- maxHeap")
    else:
        print("ERROR: not a heap")

def testHeapInsert():
    A = generateRandomList(10000, 1, 10000)
    h = MaxHeap(A)
    h.insert(10010)
    h.insert(7)
    h.insert(500)
    h.insert(-999)
    if(isMaxHeap(h.dump(False))):
        print("TEST PASSED -- maxHeap insert")
    else:
        print("ERROR: not a heap")

def testIsMaxHeap():
    A = generateRandomList(10000, 1, 10000)
    result = isMaxHeap(A) # it is highly unlikely that A is a heap
    if(result):
        print(f"ERROR: isMaxHeap returned true on an array that is almost certaintly not a heap")
    else:
        print("TEST PASSED -- isMaxHeap")

    
def testHeapGetMax():
    A = generateRandomList(10000, 1, 10000)
    h = MaxHeap(A)
    h.insert(10010)
    h.insert(7)
    h.insert(500)
    h.insert(-999)
    getResult = h.getMax()
    if((getResult == 10010) and isMaxHeap(h.dump(False))):
        print("TEST PASSED -- maxHeap getMax")
    else:
        print(f"ERROR: getResult: {getResult} ")

def testHeapExtractMax():
    A = generateRandomList(10000, 1, 10000)
    h = MaxHeap(A)
    h.insert(10010)
    h.insert(7)
    h.insert(500)
    h.insert(-999)
    extractResult = h.extractMax()
    h.extractMax()
    h.extractMax()
    if( (extractResult == 10010) and isMaxHeap(h.dump(False))):
        print("TEST PASSED -- maxHeap extractMax")
    else:
        print(f"ERROR: extractResult: {extractResult} ")

def testHeapSort():
    x = generateRandomList(10, 1, 10)
    y = heapSort(x)
    y.reverse() # MaxHeap sort will return in descending order
    if(isSorted(y)):
        print("TEST PASSED -- heapSort")
    else:
        print("ERROR: list passed to heapSort was not sorted")

testBubbleSort()
testMerge()
testMergeSort()
testIsMaxHeap()
testHeapInitialization()
testHeapInsert()
testHeapGetMax()
testHeapExtractMax()
testHeapSort()