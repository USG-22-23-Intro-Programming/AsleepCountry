def factorial(x): 
    
    y=1

    for i in range(1, x + 1):

        y = y * i

    print ("factorial" + str(x) + " okWhat")
    print (y)

def DoubleIt():
    word = input("please enter a phrase you would like to Double")
    output= ""
    for char in word:
        output = output + char * 2
    print(output)

def camelCase():


def main():
    factorial(5)
    factorial(3)

    DoubleIt()

    camelCase()

if __name__ == "__main__":
    main()




