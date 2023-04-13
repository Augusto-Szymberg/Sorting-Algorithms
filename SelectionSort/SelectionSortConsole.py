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

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
