from graphics import*
from Button import*


def main():

    win = GraphWin("Palindrome", 800, 600)
  

    Q = Button(win, Point(600, 500), Point(700, 575), "tomato", "QUIT")
    Check = Button(win, Point(350, 350), Point(450, 425), "SteelBlue1", "Check!")

    E = Entry(Point(400, 300), 30)
    E.draw(win)
    E.setSize(16)

    T = Text(Point(400, 250), "Write a potential Palindrome below!")
    T.draw(win)
    T.setSize(25)

    Tri = Text(Point(250, 500), "It's not a palindrome")
    Tri1 = Text(Point(450, 500), "It is a palindrome!")
    while True:
        t = win.getMouse()
 
        if Q.isClicked(t):

            break

        if Check.isClicked(t):
            pal = E.getText()
            length = len(pal)
            for i in range(length):
                if pal[i] != pal[length - 1 - i]:
                    Tri1.undraw()
                    Tri.undraw()
                    Tri.draw(win)
                    Tri.setSize(20)

                    break
 
                else:
 
                    Tri1.undraw()
                    Tri.undraw()
                    Tri1.draw(win)
                    Tri1.setSize(20)
                    break

    

    
    win.close()

    


if __name__ == "__main__":
    main()
