#   ____        _      _     _____            _   
#  / __ \      (_)    | |   / ____|          | |  
# | |  | |_   _ _  ___| | _| (___   ___  _ __| |_ 
# | |  | | | | | |/ __| |/ /\___ \ / _ \| '__| __|
# | |__| | |_| | | (__|   < ____) | (_) | |  | |_ 
#  \___\_\\__,_|_|\___|_|\_\_____/ \___/|_|   \__|
# By A.S.                                          
                                                 
# It similar to Merge Sort 
# Because it is a divide and conquer algorithm
# It spits a large array of data into smaller sub-arrays
# It does this by making use of a pivot element
# Its time complexity is quasilinear.

import matplotlib.pyplot as plt
import random
import time

def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    # Base case: if the sublist has 1 or 0 elements, it is already sorted
    if left < right:
        # Partition the sublist and get the pivot index
        pivot_index = partition(arr, left, right)
        # Recursively sort the left part and the right part
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)

        # Visualize the current step of the quicksort algorithm
        visualize_quicksort(arr, left, pivot_index, right)

def partition(arr, left, right):
    # Choose the pivot element (here, we use the first element)
    pivot = arr[left]
    i = left + 1
    j = right

    # Partition the sublist using the pivot
    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[left], arr[j] = arr[j], arr[left]
    return j

def visualize_quicksort(arr, left, pivot_index, right):
    # Define colors for each segment of the array
    colors = ['blue'] * left + ['red'] * (pivot_index - left) + ['green'] * (right - pivot_index) + ['blue'] * (len(arr) - right - 1)
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title("Quicksort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.1)
    plt.clf()

# Example usage:
random.seed(42)
arr = [random.randint(0, 100) for _ in range(50)]

# Record the start time
start_time = time.time()

plt.ion()
quicksort(arr)
plt.ioff()
plt.show()

# Record the end time and calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")
