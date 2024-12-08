import os

directory = '.'  # Current directory
files = os.listdir(directory)

file_sizes = []
for file in files:
    if os.path.isfile(file):
        size = os.path.getsize(file)
        file_sizes.append((file, size))


with open('file_sizes.txt', 'w') as output_file:
    for file, size in file_sizes:
        output_file.write(f"{file}: {size} bytes\n")

# Example print to show the process
print("Sorted file sizes:", file_sizes)
