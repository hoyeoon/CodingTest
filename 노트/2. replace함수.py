# 문자열에서 ...... <- 이런식으로 되어있는 것들을 . 하나로 바꿔줌.
while '..' in answer:
    answer = answer.replace('..', '.')