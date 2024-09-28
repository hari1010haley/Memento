'''
1. 아이디어:
-파이썬은 기본적으로 대문자를 소문자보다 작다고 간주
-sorted함수 이용하여 오름차순으로 정렬가능 ( 대문자 -> 소문자 )
-역행 리턴은 reverse=True 로 설정

2. 시간복잡도:
- O(n log n)

3. 작업구조도:
- 문자열 입력받기
- 내림차순 정렬 : sorted 함수와 reverse=True를 이용
- 리스트 -> 문자열 변환 : ''.join
- 결과출력

'''


import sys

def solution(s):
    return ''.join(sorted(s, reverse=True))


def valid_input():
    while True:
        s = sys.stdin.readline().strip()
        if len(s) < 1:
            print("입력값은 최소 1자 이상이어야 합니다. 다시 입력해주세요.")
        elif not s.isalpha() or not s.isascii():
            print("입력값은 영문 대소문자만 포함되어야 합니다. 다시 입력해주세요.")
        else:
            return s

if __name__ == "__main__":
    print('s문자열을 입력하세요:')
    s = valid_input()
    print('정렬된 결과:', solution(s))

