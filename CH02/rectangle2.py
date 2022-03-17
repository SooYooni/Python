import turtle as t
t.shape("turtle")
t.color("green")
t.bgcolor("skyblue")

t.fillcolor("turquoise")
#t.begin_fill()
for i in range(0, 100):
    t.forward(10 + i)
    t.right(30 + i)
    print("i = ", i)

#t.end_fill()   t.begin_fill()이랑  t.end_fill()이랑 같이 써야됨(안에 색깔 변경)

'''t.forward(100)
t.right(90)

t.forward(100)
t.right(90)

t.forward(100)
t.right(90)
'''
t.done()


'''
t.speed(1)
for i in range(300):
    t.fd(i)
    t.rt(91)

t.done()
'''