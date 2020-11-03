#Insertion sort

# Algorithm
# To sort an array of size n in ascending order:
# 1: Iterate from arr[1] to arr[n] over the array.
# 2: Compare the current element (key) to its predecessor.
# 3: If the key element is smaller than its predecessor, compare it to the elements before.
# Move the greater elements one position up to make space for the swapped element.

# Time Complexity: O(n^2)
#
# Auxiliary Space: O(1)
#
# Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
#
# Algorithmic Paradigm: Incremental Approach
#
# Sorting In Place: Yes

def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i-1
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    print("sorted list:",arr)

arr = [4,3,2,1]
insertionSort(arr)


