 # Pracice with sorting algorithms

 # HEAP SORT
def parent(i):
    # Return the parent of node at index i
    return i//2 - 1

def left(i):
    # Return the left child of node at index i
    return 2 * i + 1

def right(i):
    # Return the right child of node at index i
    return 2 * i + 2

def max_heapify(A, n, i):
    # Assume left and right are max heaps, so float the root down
    # if it violates the max heap property
    l = left(i)
    r = right(i)
    largest = i

    if  l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)

def build_max_heap(A, n):
    # Convert A into a max heap
    for i in range(len(A)//2 - 1, -1, -1):
        max_heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    build_max_heap(A, n)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        n -= 1
        max_heapify(A, n, 0)

def main():
    A = [5,13,25,7,17,20,8,4]
    print(A)
    heap_sort(A)
    print(A)

if __name__ == "__main__":
    main()
 
 #HEAP-MINIMUM, HEAP-EXTRACT-MIN, HEAP-DECREASE-KEY, and MIN-HEAP-INSERT