# input = [1,2,3,4,5,6]

# User input
str_input = input("Enter a list of numbers separated by spaces: ")
input_lst = [int(x) for x in str_input.split()]


# change input_lsts to input if using preset string
for i in input_lst:
    if i % 2 == 0:
        print(i*i)