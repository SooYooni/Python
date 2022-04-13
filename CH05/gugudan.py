# 2, 4, 6, 8 단의 구구단을 출력하는 프로그램
for x in range(2, 10, 2):
    for y in range(1, 10):
        print(x, '*', y, '=', x*y)
    print('-----------------')