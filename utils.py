import random

def isSorted(l):
    srted = True
    for i in range(len(l) - 1):
        if(l[i] > l[i+1]):
            srted = False
            break
    return srted

def isMaxHeap(l, debug=False):
    for i in range(len(l) // 2):
        if(2*(i+1) < len(l) ): # need to check in order to avoid index out of range error
            if(l[i] < l[2*(i+1) - 1] or l[i] < l[2*(i+1)]):
                if(debug):
                    print(f"ERROR Not a heap -- bad index is: {i}")
                return False
        else:
            if(l[i] < l[2*(i+1) - 1]):
                if(debug):
                    print(f"ERROR Not a heap -- bad index is: {i}")
                return False            
            
    return True
 
def swap(l, i):
    temp = l[i]
    l[i] = l[i-1]
    l[i-1] = temp
    return l

def generateRandomList(n, lowerBound, upperBound):
    l = []
    for i in range(n):
        l.append(random.randint(lowerBound,upperBound))
    return l

def merge(l1, l2, debug=False):
    if(not(isSorted(l1) and isSorted(l2))):
        if(debug):
            print("merge: ERROR at least one list is not sorted. Lists must be sorted for merge to work")
            return [] 
    result = []
    i1 = 0
    i2 = 0
    for i in range(len(l1) + len(l2)):

        # when l1 is complete index will be out of range
        if(i1 >= len(l1)):
            val2 = l2[i2]
            result.append(val2)
            i2 += 1
            continue
        else: 
            val1 = l1[i1]
        
        # when l2 is complete index will be out of range
        if(i2 >= len(l2)):
            val1 = l1[i1]
            result.append(val1)
            i1 += 1
            continue
        else: 
            val2 = l2[i2]
        
        if(val1 < val2):
            result.append(val1)
            i1 += 1
        else:
            result.append(val2)
            i2 += 1
    return result
