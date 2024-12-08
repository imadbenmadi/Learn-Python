import os

txt_files = []
for file in os.listdir('.'):
    if file.endswith('.txt'):
        txt_files.append(file)

file_report = {}

for file in txt_files:
    with open(file, 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
        file_report[file] = line_count

with open('report.txt', 'w') as report_file:
    for file, count in file_report.items():
        report_file.write(f"{file} : {count} lines\n")

print("File report:", file_report)
