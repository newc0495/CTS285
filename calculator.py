def getInput():
    num = int(input("Enter a number: "))
    return num

def add(num1, num2):    
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mainMenu():
    menu = {}
    menu[1] = "Add"
    menu[2] = "Subtract"
    menu[3] = "Multiply"
    menu[4] = "Divide"
    menu[5] = "Exit"
    for option in menu:
        print(option, menu[option])
    choice = getInput()
    if choice == 1:
        print()
        print("Add")
        num1 = getInput()
        num2 = getInput()
        print(num1, "+", num2, "=", add(num1, num2))
        repeat()
    elif choice == 2:
        print()
        print("Subtract")
        num1 = getInput()
        num2 = getInput()
        print(num1, "-", num2, "=", sub(num1, num2))
        repeat()
    elif choice == 3:
        print()
        print("Multiply")
        num1 = getInput()
        num2 = getInput()
        print(num1, "*", num2, "=", mul(num1, num2))
        repeat()
    elif choice == 4:
        print()
        print("Divide")
        num1 = getInput()
        num2 = getInput()
        print(num1, "/", num2, "=", div(num1, num2))
        repeat()
    elif choice == 5:
        print()
        print("Goodbye.")
    else:
        print("Not a valid choice.")
        print()
        mainMenu()

def repeat():
    repeat = {}
    repeat[1] = "Main Menu"
    repeat[2] = "Exit"
    for option in repeat:
        print(option, repeat[option])
    choice = getInput()
    if choice == 1:
        print()
        mainMenu()
    elif choice == 2:
        print("Goodbye.")
    else:
        print("Not a valid choice.")
        print()
        repeat()
        
mainMenu()
