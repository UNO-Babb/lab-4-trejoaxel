#TurtleGraphics.py
#Name: Axel
#Date: 02/15/2025
#Assignment: Lab 4

hideturtle()

def drawSquare(hotdog, size):
    for i in range(4):
        hotdog.forward(size)
        hotdog.right(90)

def drawPolygon(hotdog, sides):
    for s in range(sides):
        hotdog.forward(50)
        hotdog.right(360/sides)

def fillCorner(hotcat, corner):
    #draw big square
    drawSquare(hotcat, 100)
    
    if corner == 1:
        hotcat.begin_fill()
        drawSquare(hotcat, 50)
        hotcat.end_fill()
    elif corner == 2:    
        hotcat.forward(50)
        hotcat.begin_fill()
        drawSquare(hotcat, 50)
        hotcat.end_fill()
    elif corner == 3:
        hotcat.right(90)
        hotcat.forward(50)
        hotcat.left(90)
        hotcat.begin_fill()
        drawSquare(hotcat, 50)
        hotcat.end_fill()
        
def squaresInSquares(hotfrog, multi):
    #draw bigger square
    hotfrog.penup()
    hotfrog.left(135)
    hotfrog.forward(141.5)
    hotfrog.pendown()
    hotfrog.right(135)
    drawSquare(hotfrog, 200)
    
   # if m in range(multi):
        
    
    
def main():
    hotdog = turtle.Turtle()
    
    #drawPolygon(hotdog, 5) #draws a pentagon
    #drawPolygon(hotdog, 8) #draws an octogon 
    #drawPolygon(hotdog, 3) #draws a triangle
    
    #fillCorner(hotdog, 2) #draws a square with top right corner filled in.
    #fillCorner(hotdog, 3) #draws a square bottom left corner filled in.


    squaresInSquares(hotdog, 5) #draws 5 concentric squares
    #squaresInSquares(hotdog, 3) #draws 3 concentric squares


main()
