d = {}

with open("059.fasta", 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        line = line.strip()
        for s in line:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

print(d)
