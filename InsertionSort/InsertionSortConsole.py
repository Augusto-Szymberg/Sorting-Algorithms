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

def insertion_sort(arr):
    # Iterate through the array starting from 1 to the end
    for i in range(1, len(arr)):
        # The current element to be compared and potentially inserted at a new position
        key = arr[i] # Current compare element
        j = i - 1 # Index for previous element

        # Iterate backwards from the current element (key) towards the beginning of the array
        # Determine if the previous element is greater than the key
        while j >= 0 and key < arr[j]:
            # If the previous element is greater, move it one position to the right
            arr[j + 1] = arr[j]
            # Move to the next previous element (move left)
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

insertion_sort(arr)
print("Sorted array:", arr)
                                     
                                                                    