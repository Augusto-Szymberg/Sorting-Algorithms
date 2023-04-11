#  ____        _     _     _       _____            _   
# |  _ \      | |   | |   | |     / ____|          | |  
# | |_) |_   _| |__ | |__ | | ___| (___   ___  _ __| |_ 
# |  _ <| | | | '_ \| '_ \| |/ _ \\___ \ / _ \| '__| __|
# | |_) | |_| | |_) | |_) | |  __/____) | (_) | |  | |_ 
# |____/ \__,_|_.__/|_.__/|_|\___|_____/ \___/|_|   \__|
# By A.S.

# This is one of the most intuative and basic sorting algorithms
# The problem with this algorithm is that it is very slow.
# This is because its time complexity is quadratic.
# That means that it gets slower and slower as the list gets longer.
# This file contains a graphical interfaze to demostrate how it works.

import matplotlib.pyplot as plt
import random
import time

def visualize(arr, title):
    plt.bar(range(len(arr)), arr)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show(block=False)
    plt.pause(0.01)
    plt.clf()

def bubble_sort_visualized(arr):
    n = len(arr)

    # Initial visualization
    visualize(arr, "Original Array")

    # Start the timer
    start_time = time.time()

    # Goes through all elements in the array
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            # Visualize the current state of the array after the swap
            visualize(arr, f"Sorting - Pass {i+1}")

    # End timer
    end_time = time.time()
    duration = end_time - start_time

    # Final visualization
    visualize(arr, "Sorted Array")
    plt.close()

    return duration

# Creates a random array and fills it with 30 random elements
arr = []
for _ in range(30):
    arr.append(random.randint(1, 100))

# Perform the bubble sort and visualize the process
sorting_duration = bubble_sort_visualized(arr)

print(f"Sorting duration: {sorting_duration:.2f} seconds")
