import turtle 

  

def draw_circle(turtle, color, x, y, radius): 

  turtle.penup() 

  turtle.color(color) 

  turtle.fillcolor(color) 

  turtle.goto(x,y) 

  turtle.pendown() 

  turtle.begin_fill() 

  turtle.circle(radius) 

  turtle.end_fill() 

     

def draw_triangle(turtle, color, x, y, size): 

  turtle.penup() 

  turtle.color(color) 

  turtle.fillcolor(color) 

  turtle.goto(x,y) 

  turtle.pendown() 

  turtle.begin_fill() 

  for i in range (3): 

    turtle.forward(size) 

    turtle.left(120) 

  turtle.end_fill() 

  turtle.setheading(0) 
