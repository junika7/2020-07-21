Seq1 = 'ATGTTATAG'

#for i in range(len(Seq1)): #내가 한 것
#    if i % 3 == 0:
#        print(Seq1[i])

for i in range(0, len(Seq1), 3):
    #print(i) #0, 3, 6
    print(i, Seq1[i]) #인덱싱
