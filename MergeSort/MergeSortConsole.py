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
# A problem is that it requires extra memory

def merge_sort(arr):
    # Base case: if the list has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves and return the result
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare and merge the elements from left and right lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left list
    result += left[i:]
    # Append any remaining elements from the right list
    result += right[j:]

    return result

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
