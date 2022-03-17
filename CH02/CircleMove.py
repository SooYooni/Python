import turtle as t

n = int(input("circle number : "))
t.shape("turtle")
t.speed(50)

for i in range(n):
    t.circle(100)
    t.forward(10)

t.done()


