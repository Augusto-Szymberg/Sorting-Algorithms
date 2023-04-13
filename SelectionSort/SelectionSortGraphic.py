#   _____      _           _   _              _____            _   
#  / ____|    | |         | | (_)            / ____|          | |  
# | (___   ___| | ___  ___| |_ _  ___  _ __ | (___   ___  _ __| |_ 
#  \___ \ / _ \ |/ _ \/ __| __| |/ _ \| '_ \ \___ \ / _ \| '__| __|
#  ____) |  __/ |  __/ (__| |_| | (_) | | | |____) | (_) | |  | |_ 
# |_____/ \___|_|\___|\___|\__|_|\___/|_| |_|_____/ \___/|_|   \__|
# By A.S.                                                     
                                                                  
# Similar to the Insertion Sort Algorithm, intuative and basic.
# It is also very slow due to its time compelxity being quadratic.
# This means that the longer the input array the slower and slower the program gets.
# This file contains a graphical interfaze to demostrate how it works.

import matplotlib.pyplot as plt
import random
import time

def visualize(arr, i, j, min_index):
    plt.clf()
    bar_colors = ['blue'] * len(arr)
    bar_colors[i] = 'red'
    bar_colors[min_index] = 'green'
    if j is not None:
        bar_colors[j] = 'yellow'

    plt.bar(range(len(arr)), arr, color=bar_colors)
    plt.title("Selection Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.1)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        visualize(arr, i, None, min_index)
        for j in range(i+1, n):
            visualize(arr, i, j, min_index)
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            visualize(arr, i, None, min_index)

    return arr

# Generate an array of 20 random elements between 1 and 100
arr = [random.randint(1, 100) for _ in range(20)]

# Visualize the sorting process
plt.ion()
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
plt.ioff()
plt.show()
