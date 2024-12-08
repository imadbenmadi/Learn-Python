numbers = list(range(1, 21))

squares = list(map(lambda x: x ** 2, numbers))
squares = list(map(lambda x: x ** 2, numbers))

filtered_numbers = list(filter(lambda x: x % 3 != 0, numbers))
squares_of_filtered_numbers = list(map(lambda x: x ** 2, filtered_numbers))
cubes = [x ** 3 for x in filtered_numbers]

print("Original numbers:", numbers)
print("Filtered numbers:", filtered_numbers)
print("Squares of filtered numbers:", squares_of_filtered_numbers)
print("Cubes of filtered numbers:", cubes)

L  = [12,12,1,2]
L.insert(0,1)
s = sort(L,key = lambda  x >2   )