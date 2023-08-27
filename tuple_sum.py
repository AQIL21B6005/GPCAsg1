# tup = (1, 2, 9, 8)
# tup[0] = 1

# lst = [1, 2,3]
# lst[0] = 2
# print(tup)
# print(lst)

tup_input = input("Enter elements for the tuple separated by spaces: ")
tup = tuple(map(int, tup_input.split()))

# Input for the initial list
lst_input = input("Enter elements for the list separated by spaces: ")
lst = list(map(int, lst_input.split()))

print("Updated tuple:", tup)
print("Updated list:", lst)

def sum_tuple(tup_sum):
    t = list(tup_sum)
    
    count = 0

    for i in t:
        count += i
    return count

# tup_sum = (1, 2, 10, 9)

tup_sum_input = input("Enter elements for the tuple to calculate sum separated by spaces: ")
tup_sum = tuple(map(int, tup_sum_input.split()))

print("Sum of elements in the tuple:", sum_tuple(tup_sum))

print(sum(tup_sum))