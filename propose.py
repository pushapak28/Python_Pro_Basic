# before running this just install -->  pip install PythonTurtle 
# python.exe -m pip install --upgrade pip



from turtle import *
import turtle as tur  

turt = tur.Turtle()
tur.title("Pythontpoint")

def curve():
    for i in range(200):  
        # Defining step by step curve motion
        turt.right(1)
        turt.forward(1)
def heart():
  
    # Set the fill color to red
    turt.fillcolor('red')
  
    # Start filling the color
    turt.begin_fill()
  
    turt.left(140)
    turt.forward(113)
  
    curve()
    turt.left(120)
  
    # Draw the right curve
    curve()
  
    turt.forward(112)
    turt.end_fill()
  
def txt():
 
    turt.up()
    turt.setpos(-68, 95)
    turt.down()
    turt.color('cyan')
    turt.write("I Love You", font=(
      "Times New Roman", 12, "bold"))
  
  
# Draw a heart
heart()
  
# Write text
txt()
  
# To hide turtle
tur.ht()
tur.done()
