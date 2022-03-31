# 정수를 입력받아 그 수가 짝수인지 홀수인지 판별하고 "q"를 입력받으면 종료하는 프로그램.

while True:
    a = int(input('input value? '))
    if a == 'q':
        print('exit')
        break
    else:
        a = int(a)
        if a % 2 == 0:
            print("a는 짝수")
        else:
            print("a는 홀수")