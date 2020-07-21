line_count = 0
n = 0

with open("061.fastq", 'r') as handle:
    for line in handle:
        if n % 4 == 1:
            line_count += len(line.strip())
        n += 1

print(line_count)

