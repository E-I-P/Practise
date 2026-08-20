# indexing = accessing elements of a sequence using their index

name = "John"
print(name[0])  # accesses the first element of the string
print(name[1])  # accesses the second element of the string
print(name[2])  # accesses the third element of the string
print(name[3])  # accesses the fourth element of the string

print(name[0:2])  # accesses a slice of the string from index 0 to 1
print(name[1:3])  # accesses a slice of the string from index 1 to 2
print(name[2:4])  # accesses a slice of the string from index 2 to 3

print(name[-1])  # accesses the last element of the string
print(name[-2])  # accesses the second to last element of the string
print(name[-3])  # accesses the third to last element of the string
print(name[-4])  # accesses the fourth to last element of the string

print(name[::-1])  # accesses the string in reverse order
print(name[::2])  # accesses every second element of the string