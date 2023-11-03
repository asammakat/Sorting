from utils import swap, merge
from heap import MaxHeap

def bubbleSort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1, i, -1):
            if(l[j] < l[j-1]):
                swap(l, j)
    return l

def mergeSort(l):
    chunk1 = l[0:(len(l)//2)]
    chunk2 = l[(len(l)//2 ):len(l)]
    if(len(chunk1) > 1):
        sortedChunk1 = mergeSort( chunk1 )
    else:
        sortedChunk1 = chunk1
    
    if(len(chunk2) > 1):
        sortedChunk2 = mergeSort( chunk2 )
    else:
        sortedChunk2 = chunk2
        
    result = merge(sortedChunk1, sortedChunk2)
    return result

def heapSort(l):
    h = MaxHeap(l)
    result = h.getSorted()
    return result