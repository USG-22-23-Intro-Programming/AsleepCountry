def greeting():
    print("Hello")
    answer=input("Please enter your name")
    print("Hello" + answer)
    print(answer,"is it? It is nice meet you!")
    print("Have a good day")

def isMultiple(x,y):
    if x % y == 0:
        print(str(x)+ " is a multiple of " + str(y))
    else:
        print(str(x)+ " is not a multiple of " + str(y))

def palindrome():
    s = input("Type in a palindrome you want to test")
    length= len(s)
    #for loop to repeat
    #i starts at 0, and it adds one each time
    for i in range(length):
        if s[i] != s[length - 1 - i]:
            return False

    return True
            
            
def main():
    greeting()
    isMultiple(4,3)

    answer = palindrome()
    print(answer)


if __name__ == "__main__":
    main()



    
    
