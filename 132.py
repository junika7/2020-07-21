import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [txt]")

f = sys.argv[1]
s = ''

with open(f, 'r') as handle:
    for line in handle:
        line = line.strip()
        s += line
    print(s)

