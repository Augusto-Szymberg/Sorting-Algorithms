#  _____                     _   _              _____            _   
# |_   _|                   | | (_)            / ____|          | |  
#   | |  _ __  ___  ___ _ __| |_ _  ___  _ __ | (___   ___  _ __| |_ 
#   | | | '_ \/ __|/ _ \ '__| __| |/ _ \| '_ \ \___ \ / _ \| '__| __|
#  _| |_| | | \__ \  __/ |  | |_| | (_) | | | |____) | (_) | |  | |_ 
# |_____|_| |_|___/\___|_|   \__|_|\___/|_| |_|_____/ \___/|_|   \__|
# By A.S

# This is an intuative and basic sorting algorithm.
# This algorithm is only good when the input data is already mostly sorted.
# But for completly unsorted data it is still very slow.
# This is because its time complexity is quadratic.
# That means that the more data the slower and slower it gets.
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

def insertion_sort_visualized(arr):
    # Start timer
    start_time = time.time()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Initial visualization
        visualize(arr, "Original Array")

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

            # Visualize the current state of the array after shifting the elements
            visualize(arr, f"Sorting - Index {i}")

        arr[j + 1] = key

    # End timer
    end_time = time.time()
    duration = end_time - start_time

    # Final visualization
    visualize(arr, "Sorted Array")
    plt.close()

    return duration

# Generate a random array with 30 elements using a normal for loop
arr = []
for _ in range(30):
    arr.append(random.randint(1, 100))

# Perform the insertion sort and visualize the process
sorting_duration = insertion_sort_visualized(arr)

print(f"Sorting duration: {sorting_duration:.2f} seconds")
