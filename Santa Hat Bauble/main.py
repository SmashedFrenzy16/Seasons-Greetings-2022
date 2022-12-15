from turtle import * 

from shapes import * 

from random import randint 

  

myPen = Turtle() 

myPen.shape("turtle") 

myPen.speed("fastest") 

  

window = turtle.Screen() 

window.bgcolor("#FFFFFF") 

  

  

draw_circle(myPen, "#69D9FF", 0, -200, 200) 

  

draw_triangle(myPen, "#Ff0000", -120, -70, 250) 

  

draw_circle(myPen, "#FFFFFF", 5, 120, 20) 

  

circleLoop = 8 

  

myPen.up() 

  

myPen.goto(-120, -75) 

  

myPen.down() 

  

for i in range(1, 14): 

   

  myPen.down() 

   

  myPen.begin_fill() 

   

  myPen.circle(20) 

   

  myPen.end_fill() 

   

  myPen.up() 

   

  myPen.fd(20) 

   

myPen.up() 

  

myPen.goto(-125, -158) 

  

myPen.down() 

  

myPen.color("black") 

  

myPen.write("Season's Greetings", font=("Arial", 

                                    20, "bold")) 

myPen.hideturtle() 
