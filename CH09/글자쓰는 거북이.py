# 글자쓰는 거북이 #
import tkinter
#import tkinter as tk
from tkinter.simpledialog import *
from turtle import  *

import turtle as t
from turtle import *

swidth, sheight = 300, 300
txtSize = 30
t.shape('turtle')
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)

retStr = tkinter.simpledialog.askstring('input char', 'input for turtle')
t.write(retStr, font=('맑은고딕', txtSize, 'bold'))

t.done()