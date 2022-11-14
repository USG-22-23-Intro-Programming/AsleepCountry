from graphics import*
from Button import*


def main():

    win = GraphWin("character creator", 800, 600)
    win.setBackground("lightsteelblue")

    C = Circle(Point(300, 300), 150)
    C.draw(win)

    #R = Rectangle(Point(200, 500), Point(400, 575))
    #R.draw(win)

    #L = Line(Point(0, 0), Point(800, 600))
    #L.draw(win)

    BigEye1 = Circle(Point(200, 250), 50)
    BigEye2 = Circle(Point(400, 250), 50)

    smallEye1 = Circle(Point(250, 250), 20)
    smallEye2 = Circle(Point(350, 250), 20)

    thirdEye = Circle(Point(300,200),25)

    hat1 = Rectangle(Point(150, 150), Point(300, 200))
    hat2 = Rectangle(Point(450, 150), Point(300, 200))
    hat3 = Rectangle(Point(375, 150), Point(250, 100))

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Big Eyes")
    B2 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Small Eyes")
    B3 = Button(win, Point(600, 400), Point(700, 475), "violet", "third eye?")
    B4 = Button(win, Point(600, 500), Point(700, 575), "light blue", "HAT!!")
    

    Q = Button(win, Point(600, 300), Point(700, 375), "lavenderblush", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            
            BigEye1.draw(win)
            BigEye2.draw(win)

        if B2.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            BigEye1.undraw()
            BigEye2.undraw()
            
            smallEye1.draw(win)
            smallEye2.draw(win)

        if B3.isClicked(m):
            thirdEye.undraw()

            thirdEye.draw(win)

        if B4.isClicked(m):
            hat1.undraw()
            hat2.undraw()
            hat3.undraw()

            hat1.draw(win)
            hat2.draw(win)
            hat3.draw(win)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
