import sys

Seq1 = sys.argv[1]

for i in range(0, len(Seq1), 1):
    if Seq1[i:i+2] == "TT":
        print(i, i+1, Seq1[i:i+2])

print(Seq1.index("TT")) #처음 TT 읽으면 그 뒤부터 다시 읽어서 겹친 부분 파악 안 됨
