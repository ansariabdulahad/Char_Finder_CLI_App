# Print first char 
def findFirstChar(string) : 
    firstChar = string[0]
    print(f"Your first char from {string} is : {firstChar}")
# findFirstChar()

def findLastChar(string) : 
    lastChar = string[len(string)-1]
    print(f"Your last char from {string} is : {lastChar}")
# findLastChar()

def findCustomChar(string) :
    index = int(input("Enter your index number : \n"))
    print(f"Your custom character from {string} is : {string[index]}")


def charFinderApp() : 
    print("*** Character Finder App ***")
    string = input("Enter your string : \n")
    print("Choose an option : \n")
    print("1. Find the first character. \n")
    print("2. Find the last character. \n")
    print("3. Find the custom character. \n")

    option = int(input("Enter your option : \n"))

    if option == 1 : findFirstChar(string)
    elif option == 2 : findLastChar(string)
    elif option == 3 : findCustomChar(string)
    else : print("You had choosed wrong option")
charFinderApp()