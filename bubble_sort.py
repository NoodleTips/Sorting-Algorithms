
def bubble_sort(array):
    n = len(array)
    
    for i  in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
user_input = input("Please enter numbers seperated by spaces: ")
user_array = [int(x) for x in user_input.split()]

bubble_sort(user_array)
print("Sorted Array:", user_array)












