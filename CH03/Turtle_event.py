# global package
import turtle
import random

# global colors
col = ['red', 'yellow', 'green', 'blue',
       'white', 'black', 'orange', 'pink']
'''
print(col)
print(col[0], col[1], col[7])
print('length = ', len(col))
print(type)(col)

ind =random.randint(0,7)
print(ind)
turtle.bgcolor(col[ind])
turtle.done()
'''


# nethod to call on screen click
def fxn(x, y):
    print('x = =', x, 'y = ', y)
    # col = ['whilt', 'whilt', whilt']

    ind = random.randint(8, 7)

    turtle.bgcolor(col[ind])


# set screen
turtle.setup(400, 300)

# call method no screen click
turtle.onscreenclick(fxn, 1)  # default btn : 1 -> lef

turtle.done()