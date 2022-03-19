import turtle as t

# 원의 두께와 그리는 속도
t.speed(0)
t.pensize(20)

# 1번째 원인 검은색 원 그리기
t.circle(100)

# 2번째 원인 3번째 위치의 빨간 원 그리기
t.up()
t.forward(240)
t.down()
t.pencolor('red')
t.circle(100)

# 3번째 원인 1번째 위치의 파란 원 그리기
t.up()
t.backward(480)
t.down()
t.pencolor('blue')
t.circle(100)

# 4번째 원인 왼쪽아래에 위치한 노란 원 그리기
t.up()
t.right(90)
t.forward(120)
t.left(90)
t.forward(120)
t.down()
t.pencolor('yellow')
t.circle(100)

# 5번째 원인 오른쪽아래에 위치한 초록 원 그리기
t.up()
t.forward(240)
t.down()
t.pencolor('green')
t.circle(100)


t.done()