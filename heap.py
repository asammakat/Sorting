class MaxHeap:
    def __init__(self, A):
        self.array = A
        self.size = len(self.array)
        self.__buildMaxHeap()
    
    def __parent(self, i):
        return (i + 1) // 2 - 1
    
    def __left(self, i):
        return 2 * (i + 1) - 1

    def __right(self, i):
        return 2 * (i + 1)
    
    def __swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp
    
    def __heapify(self, i):
        leftNode = self.__left(i)
        rightNode = self.__right(i)
        largest = i
        if(leftNode < self.size and self.array[leftNode] > self.array[largest]):
            largest = leftNode
        if(rightNode < self.size and self.array[rightNode] > self.array[largest]):
            largest = rightNode
        if(largest == i):
            return
        self.__swap(i, largest)
        self.__heapify(largest)

    def __buildMaxHeap(self):
        for i in range( self.size // 2 - 1, -1, -1):
            self.__heapify(i)
        
    def insert(self, e):
        self.array.append(e)
        self.size += 1
        i = self.size - 1
        while (i > 0 and self.array[i] > self.array[self.__parent(i)]):
            self.__swap(i, self.__parent(i))
            i = self.__parent(i)
        
    def getMax(self):
        return self.array[0]
    
    def extractMax(self):
        result = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.__heapify(0)
        return result

    def getSorted(self):
        result = []
        for i in range(self.size):
            result.append(self.extractMax())
        return result
    
    def dump(self, display):
        if(display):
            print(self.array[0:self.size])
        return self.array[0:self.size]
    