 # Pracice with sorting algorithms

# HEAP SORT - with MAX HEAP
def parent(i):
    # Return the parent of node at index i
    return (i-1)//2

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

# HEAP SORT - with MIN HEAP
def min_heapify(A, n, i):
    # Assume left and right are min heaps, so float i down
    # if it violates the min heap property
    l = left(i)
    r = right(i)
    smallest = i

    if  l < n and A[l] < A[smallest]:
        smallest = l
    if r < n and A[r] < A[smallest]:
        smallest = r
    
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, n, smallest)

def build_min_heap(A, n):
    # Convert A into a min heap
    for i in range(len(A)//2 - 1, -1, -1):
        min_heapify(A, n, i)

def min_heap_sort(A):
    # Sort a list using a min heap
    n = len(A)
    build_min_heap(A, n)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        min_heapify(A, n, 0)

def heap_minimum(A):
    # Return the minimum value of the min heap
    return A[0]

def heap_extract_min(A):
    # Extract the minimum value, add it to the end of the list, 
    # reheapify, and then return the value
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    min_heapify(A, len(A) - 1, 0)
    return A[-1]

def heap_decrease_key(A, i, key):
    # Change the value of i to key, then reheapify
    A[i] = key
    min_heapify(A, len(A), parent(i)) 

def min_heap_insert(A, key):
    # Insert a key into the min heap and maintain 
    # the min heap property
    A.append(key)
    curr = len(A) - 1
    p = parent(curr)
    print("parent, curr =", p, curr)
    while curr > 0 and A[curr] < A[p]:
        A[p], A[curr] = A[curr], A[p]
        curr = p
        p = parent(p)
 

def main():
    A = [5,13,25,7,17,20,8,4]
    print(A)
    build_min_heap(A, len(A))
    print(A)
    min_heap_insert(A, 6)
    print(A)

if __name__ == "__main__":
    main()
