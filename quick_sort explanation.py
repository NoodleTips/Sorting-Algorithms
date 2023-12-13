
#  ! This is just the explanation page, not the action functioning code!

# * 1 ************************
# array
x = [12,5,9,3,2,7]

# choose a pivot number
# Example "5"



# * 2 ************************
#  partition the array into elemets less than 5 and greater than 5

[3,2] | [5] | [12,9,7]


# * 3 ************************
# Apply quicksort recursively to each sub-array

# left sub-array: 
[3,2]

# right sub-array: 
[12,9,7]


# * 4 ************************
# select a new pivot for left sub-array

# 2

[2] | [3]

# * 5 ************************
# # select a new pivot for right sub-array

# 9

[7] | [9] | [12]


# * 6 ************************

# now combine the sorted sub arrays

[2,3,5,7,9,12]
















