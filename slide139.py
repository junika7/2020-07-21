import sys
import json

def read_csv(file_name: str) -> list:
    ret = [] #빈 list 설정
    with open(file_name, 'r') as handle:
        for line in handle:
            splitted = line.strip().split(",") #line들에 대해서 가공해서 splitted로 지정하고
            ret.append(splitted) #가공한 splitted를 빈 list인 ret에 추가
        d = dict(zip(ret[0], ret[1])) #list 2개로 이루어진 list인 ret에서 각각의 원소(각 list)를 dict(zip)을 이용해서 딕셔너리로 지정
        print(d) #딕셔너리 잘 만들어졌는지 확인
    return d #반환값을 d로 설정

def to_json(l: list, file_name: str) -> None: #list를 json 파일로 만드는 함수를 정의
    with open(file_name, 'w') as handle: #입력하는 파일명의 파일을 만들면서 아래 내용을 작성
        json.dump(l, handle, indent = 4) #입력받는 list를 indent 4의 json 형식으로 작성

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1]
    result_slide139 = read_csv(file_name) #slide139.csv 파일을 받을 것이므로
    print(result_slide19) #여기도 반환값인 d가 출력되므로 딕셔너리가 출력됨
    to_json(result_slide139, "slide139_to_json_result.json") #json 파일로 만들고 cat 명령으로 확인 가능
