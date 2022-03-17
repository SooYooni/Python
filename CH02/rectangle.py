'''import  turtle

turtle.shape('turtle')

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

turtle.done()
'''

import  turtle as t
t.shape('turtle')
for i in range(0, 20):
    t.forward(200 + i *10)
    t.right(90 + i * 5)

t.done()
