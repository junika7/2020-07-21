#Seq1 = 'ATGTTATAG' #내가 한 것
#print(Seq1)
#print(Seq1.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper())

import sys

def comp1(seq: str) -> str: #type hint
    comp = "" #A면 새로운 스트링에 T를 더하고 C면 G를 더하는 방식
    for s in seq:
        if s == "A":
            comp += "T"
        elif s == "C":
            comp += "G"
        elif s == "G":
            comp += "C"
        elif s == "T":
            comp += "A"
    return comp

def comp2(seq: str) -> str: #상보적인 딕셔너리를 사용하는 방식
    d_comp = {"A":"T", "T":"A", "C":"G", "G":"C"}
    comp = ""
    for s in seq:
        comp += d_comp[s]
    return comp

if __name__ == "__main__": #p028.py로 저정하고 interpreter 모드에서 import p028로 import 가능(숫자로 시작하면 import 안 됨), p028.comp1("ATGTAATAG") 처럼 사용 가능해지고, 다른 파이썬 스크립트에서도 import p028 입력 후 함수 사용 가능해짐, 이 줄 아래로는 import 했을 때는 실행 안되도록 하는 부분임!!!!! 만약 이 줄 위에 print("Hi") 있으면 import 했을 때 Hi 출력됨.
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()

    seq = sys.argv[1]
    c1 = comp1(seq)
    c2 = comp2(seq)
    print(seq)
    print(c1)
    print(c2)
