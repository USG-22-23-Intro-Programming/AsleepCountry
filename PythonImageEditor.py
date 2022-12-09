from graphics import*
from Button import*

def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]


            red = red - 45
            green = green - 45
            blue = blue - 45

            if red < 0:
                red = 0
            if blue < 0:
                blue = 0
            if green < 0:
                green = 0
           
                

            # contrast - any "light" pixel --> more light
            #any "dark" pixel --> more dark
            #print([red, green, blue])
                c = color_rgb(abs(red), abs(green), abs(blue))
                img.setPixel(i, j, c)

def lighten(img):
     x = img.getWidth()
     y= img.getHeight()

     for i in range (x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]

            red = red + 45                  
            green = green + 45
            blue = blue + 45
            
            
            if red > 255:                    
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255


            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)


def grayScale(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]                         
            green = pix[0]                       
            blue = pix[0]                      
                                                

            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)



def contrast(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            red = pix[0]                        
            green = pix[1]                      
            blue = pix[2]

            if red > 128:                    
                red = red + 15              
            if red <= 128:                  
                red = red - 15
                
            if green > 128:                  
                green = red + 15
            if green <= 128:
                green = green - 15
                
            if blue > 128:
                blue = blue + 15
            if green <= 128:
                blue = blue - 15
                
            if red > 255:                   
                red = 255                   
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255

            if red < 0:                     
                red = 0                     
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0
            
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)



        

def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("salmon")

    I = Image(Point(300, 300), "sonic.png")
    I.draw(win)

    B = Button(win, Point(600, 100), Point(700, 175), "whitesmoke", "Darken")
    B2 = Button(win, Point(600, 200), Point(700, 275), "whitesmoke", "Lighten")
    B3 = Button(win, Point(600, 400), Point(700, 475), "whitesmoke", "Contrast")
    B4 = Button(win, Point(600, 500), Point(700, 575), "whitesmoke", "Grayscale")

    Q = Button(win, Point(600, 300), Point(700, 375), "orchid", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)

        if B2.isClicked(m):
            lighten(I)

        if B3.isClicked(m):
            contrast(I)

        if B4.isClicked(m):
            grayScale(I)

        

        
            #if B2.isClicked(m):
            


            if Q.isClicked(m):
                break

    win.close()

if __name__ == "__main__":
    main()
