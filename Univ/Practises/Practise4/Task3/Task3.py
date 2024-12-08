with open('input_numbers.txt', 'r') as file:
    content = file.read()
    numbers = []
    for num in content.split():
        numbers.append(int(num))

    


def run_length_encoding(numbers):
    compressed_list = []
    count = 1
    current = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] == current:
            count += 1
        else:
            compressed_list.append((current, count))  
            current = numbers[i]
            count = 1
    
    compressed_list.append((current, count))  
    return compressed_list

compressed = run_length_encoding(numbers)

with open('compressed.txt', 'w') as output_file:
    for num, count in compressed:
        output_file.write(f"{num} : {count} times\n")  
        
print("Original numbers:", numbers)
print("Compressed list:", compressed)
