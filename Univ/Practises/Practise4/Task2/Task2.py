with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

filtered_numbers = []
for num in numbers:
    if num % 2 != 0:
        filtered_numbers.append(num)

with open('filtered_numbers.txt', 'w') as output_file:
    for num in filtered_numbers:
        output_file.write(f"{num}\n")

print("Original numbers:", numbers)
print("Filtered odd numbers:", filtered_numbers)


# vqr = 1
# file = open('numbers.txt', 'r')
# file.read()
# file.close()