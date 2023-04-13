#  __  __                      _____            _   
# |  \/  |                    / ____|          | |  
# | \  / | ___ _ __ __ _  ___| (___   ___  _ __| |_ 
# | |\/| |/ _ \ '__/ _` |/ _ \\___ \ / _ \| '__| __|
# | |  | |  __/ | | (_| |  __/____) | (_) | |  | |_ 
# |_|  |_|\___|_|  \__, |\___|_____/ \___/|_|   \__|
#                   __/ |                           
#                  |___/      
# By A.S.      

# This is a more complex sorting algorithm.
# The idea is to break the main array into sub-arrays 
# And then sort them and merge them back together.
# Its time complexity is quasilinear
# This means it is much faster for longer arrays.
# A problem is that it extra memory
# This file contains a visual representation of it.

import matplotlib.pyplot as plt
import random
import time

def merge_sort(arr, left=0, right=None):
    # Base case: if the list has 1 or 0 elements, it is already sorted
    if right is None:
        right = len(arr)

    if right - left <= 1:
        return

    # Divide the list into two halves
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)

    # Merge the sorted halves
    merge(arr, left, mid, right)

    # Visualize the merge operation
    visualize_merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    merged = []
    i, j = left, mid

    # Compare and merge the elements from left and right subarrays
    while i < mid and j < right:
        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1

    # Append any remaining elements from the left subarray
    merged.extend(arr[i:mid])
    # Append any remaining elements from the right subarray
    merged.extend(arr[j:right])

    # Update the original array with the merged subarrays
    arr[left:right] = merged

def visualize_merge(arr, left, mid, right):
    # Define colors for each segment of the array
    colors = ['blue'] * left + ['red'] * (mid - left) + ['green'] * (right - mid) + ['blue'] * (len(arr) - right)

    # Create a bar chart to visualize the merge operation
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title("Merge Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.1)
    plt.clf()

# Example usage:
random.seed(42)

# Generate a random array with 30 elements using a normal for loop
arr = []
for _ in range(30):
    arr.append(random.randint(1, 100))

# Record the start time
start_time = time.time()

# Run the merge sort algorithm with visualization
plt.ion()
merge_sort(arr)
plt.ioff()
plt.show()

# Record the end time and calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")
