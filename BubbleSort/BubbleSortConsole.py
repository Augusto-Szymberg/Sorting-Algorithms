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
                                                       
def bubble_sort(arr):
    n = len(arr)

    # Go through all elements in the array
    for i in range(n):
        # Last i elements are already in place, dont check it
        for j in range(0, n-i-1):
            # Swap if element is greater that next element
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
arr = [74, 44, 25, 13, 27, 11, 81]
print("Original array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)

