
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            
        array[j + 1] = key

user_input = input("Please enter a series of numbers seperator separated by spaces: ")
user_array = [int(x) for x in user_input.split()]

insertion_sort(user_array)
print("Sorted Array:", user_array)











