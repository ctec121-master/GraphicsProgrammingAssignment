# Module 5
#   Programming Assignment 6
#       Prob-1.py

# <YOUR NAME>

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does


from graphics import *

def main():
     win = GraphWin()
     shape = Circle(Point(50,50), 20)
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)
     for i in range(5):
          p = win.getMouse()
          c = shape.getCenter()
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
          shape.move(dx,dy)
     win.close()

main()