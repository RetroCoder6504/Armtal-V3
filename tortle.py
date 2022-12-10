from turtle import *
import LibVars

"""
s = getscreen()
t = Turtle()

while True:
  t.forward(100)
  t.right(90)
"""
def setup_turtle():
  LibVars.vars["screenT"] = getscreen()
  LibVars.vars["turtle"] = Turtle()

def fwd(n):
  LibVars.vars["turtle"].forward(int(n))

def bwd(n):
  LibVars.vars["turtle"].backward(int(n))

def right(n):
  LibVars.vars["turtle"].right(int(n))

def left(n):
  LibVars.vars["turtle"].left(int(n))

def goto(x, y):
  LibVars.vars["turtle"].goto(int(x), int(y))

def home():
  LibVars.vars["turtle"].home()

def circle(n):
  LibVars.vars["turtle"].circle(int(n))

def dot(n):
  LibVars.vars["turtle"].dot(int(n))

def bg(c):
  bgcolor(c)

def title(s):
  LibVars.vars["turtle"].title(s)

def size(x, y, o):
  LibVars.vars["turtle"].shapesize(int(x), int(y), int(o))

def pensize(n):
  LibVars.vars["turtle"].pensize(int(n))

def fillColor(c):
  LibVars.vars["turtle"].fillcolor(c)

def penColor(c):
  LibVars.vars["turtle"].pencolor(c)

def color(c, C):
  LibVars.vars["turtle"].color(c, C)

def beginFill():
  LibVars.vars["turtle"].begin_fill()

def endFill():
  LibVars.vars["turtle"].end_fill()

def shape(s):
  LibVars.vars["turtle"].shape(s)

def speed(n):
  LibVars.vars["turtle"].speed(int(n))

def up():
  LibVars.vars["turtle"].penup()

def down():
  LibVars.vars["turtle"].pendown()

def undo():
  LibVars.vars["turtle"].undo()

def clear():
  LibVars.vars["turtle"].clear()

def reset():
  LibVars.vars["turtle"].reset()

def stamp():
  LibVars.vars["lastStamp"] = LibVars.Vars["turtle"].stamp()

def clearstamp():
  LibVars.Vars["turtle"].clearstamp(LibVars.Vars["lastStamp"])

Cmds = {"fwd":[fwd, 1], "bwd" : [bwd, 1], "right" : [right, 1], "left" : [left, 1], "setupT" : [setup_turtle, 0], "goto" : [goto, 2], "home":[home, 0], "circle":[circle, 1], "dot":[dot, 1], "bg":[bg, 1], "title" : [title, 1], "size" : [size, 3], "pensize" : [pensize, 1], "fillcolor" : [fillColor, 1], "pencolor" : [penColor, 1], "color" : [color, 2], "beginfill" : [beginFill, 0], "endfill" : [endFill, 0], "shape" : [shape, 1], "speed" : [speed, 1], "up" : [up, 0], "down" : [down, 0], "undo" : [undo, 0], "clear":[clear, 0], "reset" : [reset, 0], "stamp" : [stamp, 0], "clearstamp" : [clearstamp, 0]}