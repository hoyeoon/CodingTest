# 데이터의 개수가 1,000만 개를 넘거나 탐색 범위의 크기가 1,000억 이상일 때 이진 탐색 알고리즘을 의심해보자.
# 이때 input() 함수를 사용하면 시간 초과가 날 수 있으니 sys 라이브러리의 readline()함수를 이용한다.

import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)