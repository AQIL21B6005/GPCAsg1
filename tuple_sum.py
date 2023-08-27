tup = (1, 2, 9, 8)
# tup[0] = 1

lst = [1, 2,3]
lst[0] = 2
print(tup)
print(lst)

def sum(tup_sum):
    t = list(tup_sum)
    
    count = 0

    for i in t:
        count += i
    return count

tup_sum = (1, 2, 10, 9)

print(sum(tup_sum))