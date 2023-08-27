# dict_1 = {1: "A", 2: "B"}
# dict_2 = {2: "F", 4: "C"}

# For user input
dict_1 = {}
dict_2 = {}

input1 = int(input("Enter the number of key-value pairs for dict_1: "))  # Example input 2. Any power of 2 value.
for _ in range(input1):
    key = int(input("Enter key for dict_1: "))  # Example input 1, 2
    value = input("Enter value for dict_1: ")   # Example input A, Apple, Banana, B
    dict_1[key] = value

input2 = int(input("Enter the number of key-value pairs for dict_2: ")) #Example input 2. Any power of 2 value.
for _ in range(input2):
    key = int(input("Enter key for dict_2: "))  # Example input 1, 2
    value = input("Enter value for dict_2: ")   # Example input A, Apple, Banana, B
    dict_2[key] = value


dict_1.update(dict_2)

print(dict_1)


