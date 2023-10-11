# install numpy from pip
import numpy as np

list1 = [1, 2, 9, 18, 13, 3, 4, 20, 6, 8]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                
# converting list into array
array_1 = np.array(list1)

# Applying Bubble Sort
bubble_sort(array_1)
print("Sorted array is:", array_1)
