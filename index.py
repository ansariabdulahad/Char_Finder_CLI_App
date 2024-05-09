# Write a program to check the length validity of password

# def checkPasswordLength() :
#     print("*** Check Password Length ***")
#     password = input("Enter Password : \n")
#     length = len(password)
#     print(f"Your password length is : {length}")
# checkPasswordLength()

# def checkDataType() : 
#     print("*** Check Data Type ***")
#     inputData = input("Enter Data Type : \n")
#     result = type(inputData).__name__ 
#     print(f"Your data type is : {result}")
# checkDataType()

def checkPasswordLength() : 
    print("*** Check Password Length ***")
    password = input("Enter 8 degit Password : \n")
    length = len(password)
    if length == 0 :
        print(f"Your password length is : {length} please enter 8 digit password")
        checkPasswordLength()
    elif length <= 8 :
        print(f"Your password length is : {length}")
    else :
        print(f"Your password length is : {length} please enter 8 digit password")
        checkPasswordLength()
checkPasswordLength()
