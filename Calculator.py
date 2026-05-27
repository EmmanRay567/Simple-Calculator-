# This is a simple calculator app in python,
# which allows the user to choose from Addition, Subtraction, Division, and multiplication. 
def Addition(UserFirstNumber, UserSecondNumber):
    return UserFirstNumber + UserSecondNumber

def subtraction(UserFirstNumber, UserSecondNumber):
    return UserFirstNumber - UserSecondNumber

def Multiplication(UserFirstNumber, UserSecondNumber):
    return UserFirstNumber * UserSecondNumber

def Division(UserFirstNumber, UserSecondNumber):
    return UserFirstNumber / UserSecondNumber


UserFirstNumber =  float (input("Please enter your first Number: "))
UserSecondNumber = float(input("Please enter your Second Number: "))

Operation = input("Please enter your operation of choice: Addition, Subtraction, Multiplication, or Division: ")

if Operation == "Addition":
    result1 = Addition(UserFirstNumber, UserSecondNumber)
    print("Your given Output is " + str(result1))

    UserChoice = input("Press y if you would like to continue with " + str(result1) + " or press n to restart: ")

    while UserChoice == "y":
        UserSecondNumber = float(input("Enter another number to add: "))
        result1 = Addition(result1, UserSecondNumber)
        print("Your given Output is " + str(result1))

        UserChoice = input("Press y to continue with " + str(result1) + " or press n to restart: ")

    if UserChoice == "n":
        print("Your results Have been refreshed!")
        UserFirstNumber = float(input("Please enter your first Number: "))
        UserSecondNumber = float(input("Please enter your Second Number: "))

        result1 = Addition(UserFirstNumber, UserSecondNumber)
        print("Your given Output is " + str(result1))

elif Operation == "Subtraction":
    result2 = subtraction(UserFirstNumber, UserSecondNumber)
    print("Your Given output is " + str(result2))
    UserChoice = input("Press y if you would like to continue with " + str(result2) + " or press n to restart: ")

    while UserChoice == "y":
        UserSecondNumber = float(input("Enter another number to subtract: "))
        result2 = subtraction(result2, UserSecondNumber)
        print("Your given Output is " + str(result2))

        UserChoice = input("Press y to continue with " + str(result2) + " or press n to restart: ")

    if UserChoice == "n":
        print("Your results have been refreshed!")
        UserFirstNumber = float(input("Please enter your first Number: "))
        UserSecondNumber = float(input("Please enter your Second Number: "))

        result2 = subtraction(UserFirstNumber, UserSecondNumber)
        print("Your given Output is " + str(result2))


elif Operation == "Multiplication":
    result3 = Multiplication(UserFirstNumber, UserSecondNumber)
    print("Your given output is " + str(result3))
    UserChoice = input("Press y if you would like to continue with " + str(result3) + " or press n to restart: ")

    while UserChoice == "y":
        UserSecondNumber = float(input("Enter another number to multiply: "))
        result3 = Multiplication(result3, UserSecondNumber)
        print("Your given Output is " + str(result3))

        UserChoice = input("Press y to continue with " + str(result3) + " or press n to restart: ")

    if UserChoice == "n":
        print("Your results have been refreshed!")
        UserFirstNumber = float(input("Please enter your first Number: "))
        UserSecondNumber = float(input("Please enter your Second Number: "))

        result3 = Multiplication(UserFirstNumber, UserSecondNumber)
        print("Your given Output is " + str(result3))



elif Operation == "Division":
    result4 = Division(UserFirstNumber, UserSecondNumber)
    print("Your Given Value is " + str(result4))
    result4 = Division(UserFirstNumber, UserSecondNumber)
    print("Your given output is " + str(result4))
    UserChoice = input("Press y if you would like to continue with " + str(result4) + " or press n to restart: ")

    while UserChoice == "y":
        UserSecondNumber = float(input("Enter another number to Divide by: "))
        result4 = Division(result4, UserSecondNumber)
        print("Your given Output is " + str(result4))

        UserChoice = input("Press y to continue with " + str(result4) + " or press n to restart: ")

    if UserChoice == "n":
        print("Your results have been refreshed!")
        UserFirstNumber = float(input("Please enter your first Number: "))
        UserSecondNumber = float(input("Please enter your Second Number: "))

        result4 = Division(UserFirstNumber, UserSecondNumber)
        print("Your given Output is " + str(result4))

else:
    print("Invalid operation.")

   
