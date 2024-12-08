import random

random_numbers = []
while len(random_numbers) < 50:
    random_numbers.append(random.randint(1, 100))

transformed_numbers = []
def transform_number(x):
    output = {
        (True, True): "FiveSeven",
        (True, False): "Five",
        (False, True): "Seven",
        (False, False): x
    }
    return output[(x % 5 == 0, x % 7 == 0)]

transformed_numbers = list(map(transform_number, random_numbers))

with open('transformed_numbers.txt', 'w') as output_file:
    for item in transformed_numbers:
        output_file.write(f"{item}\n")

print("Original random numbers:", random_numbers)
print("Transformed numbers:", transformed_numbers)
