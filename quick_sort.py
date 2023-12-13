

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]  # less than pivot
    middle = [x for x in array if x == pivot] # equal to pivot
    right = [x for x in array if x > pivot] # greater than pivot
    
    return quick_sort(left) + middle + quick_sort(right) # recursively sort left and right sub arrays

user_input = input("Please enter numbers seperated by spaces: ")

user_array = [int(x) for x in user_input.split()]  # converts input string to integer list

sorted_array = quick_sort(user_array) # calls the quick_sort function to sort the array

print("Sorted Array:", sorted_array)

