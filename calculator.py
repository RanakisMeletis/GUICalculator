# Standard Python interface to the Tk GUI toolkit
from tkinter import *


# Checking if input option is valid (valid options: 1-6)
def option_is_valid(option):
    if option.isdigit() and int(option) <= 6:
        if int(option) == 6:
            print("Bye!")
            exit()
        return True
    else:
        print("Give a valid option number please")
        return False


# Checking if input number is valid
def number_is_valid(number, valid_digits_for_a_number):
    valid_digits = 0
    for digit in number:
        if digit in valid_digits_for_a_number:
            valid_digits += 1

    if valid_digits == len(number):
        return True
    else:
        print("Give a valid number please")
        return False


# Calculating all basic arithmetic operations
def calculate(option, number1, number2):
    result = 0
    if option == 1:
        result = number1 + number2
        print("Result = ", result)
    elif option == 2:
        result = number1 - number2
        print("Result = ", result)
    elif option == 3:
        result = number1 * number2
        print("Result = ", result)
    elif option == 4:
        if number2 != 0:
            result = number1 / number2
            print("Result = ", result)
        else:
            print("You cant divide by 0")
            return number1

    return result


# Shows the main menu of the program
def display_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. GUI calculator")
    print("6. Exit")


# Displays the text of the pressed button
def button_press(number):
    global equation_text

    equation_text = equation_text + str(number)
    equation_label.set(equation_text)


# When we press equals button (=) it calculates and displays the result
def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)

        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""


# Clears everything
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


print("Welcome to the calculator!")
# All valid inputs for a number
valid_digits_for_a_number = "0123456789.-"
option = 0
result = 0

# While user don't want to use GUI calculator
while option < 5:
    print("What do you want to do?")
    display_menu()

    option = input("Enter your choice: ")

    # While option is not valid, repeat
    while not option_is_valid(option):
        option = input("Enter your choice: ")

    option = int(option)

    # Option 5 is GUI calculator, so we break from this while
    if option == 5:
        break

    number1 = input("Give the first number: ")
    # While number is not valid, repeat
    while not number_is_valid(number1, valid_digits_for_a_number):
        number1 = input("Give the first number: ")

    # Type conversion from string to float
    number1 = float(number1)

    number2 = input("Give the second number: ")
    while not number_is_valid(number2, valid_digits_for_a_number):
        number2 = input("Give the second number: ")

    number2 = float(number2)

    result = calculate(option, number1, number2)

    # There is an option to continue with the result like a normal calculator
    continueOrNot = "y"
    while continueOrNot == "y":
        continueOrNot = input("Continue with the new result? (y/n) ")
        if continueOrNot == "y":
            print("\nYou number is: ", result)
            print("What do you want to do with it?")
            display_menu()

            option = input("Enter your choice: ")

            while not option_is_valid(option):
                option = input("Enter your choice: ")

            option = int(option)

            # Option 5 is GUI calculator, so we break from this while
            if option == 5:
                break

            # We store the previous result
            number1 = result

            number2 = input("Give the second number: ")
            while not number_is_valid(number2, valid_digits_for_a_number):
                number2 = input("Give the second number: ")

            number2 = float(number2)

            result = calculate(option, number1, number2)

        # If the user doesn't want to continue with the result, he continues from the start
        elif continueOrNot == "n":
            print("\nContinue from the start!")
            result = 0
            break
        else:
            print("Give a valid value. 'y' for yes 'n' for no")
            continueOrNot = "y"


# Creation of the main window
window = Tk()
window.title("Calculator")
window.geometry("430x600")

equation_text = ""

equation_label = StringVar()

# If the user chooses to open the GUI calculator, it continues with the last result, if there is one
if result != 0:
    equation_text = equation_text + str(result)
    equation_label.set(equation_text)

# Creation of the "screen" in GUI calculator
label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=28, height=2)
label.pack()

frame = Frame(window)
frame.pack()

buttons = []
buttons_number = -1

# Creation of the buttons
for x in range(0, 3):

    for y in reversed(range(0, 3)):
        buttons_number += 1

        buttons.append(Button(frame, text=9 - buttons_number, height=4, width=9, font=35, bg="grey",
                              command=lambda buttons_number=buttons_number: button_press(9 - buttons_number)))
        buttons[buttons_number].grid(row=x, column=y)

button0 = Button(frame, text=0, height=4, width=9, font=35, bg="grey",
                 command=lambda: button_press(0))
button0.grid(row=3, column=1)

plus = Button(frame, text='+', height=4, width=9, font=35, bg="AntiqueWhite3",
              command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, bg="AntiqueWhite3",
               command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, bg="AntiqueWhite3",
                  command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, bg="AntiqueWhite3",
                command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35, bg="AntiqueWhite3",
               command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35, bg="AntiqueWhite3",
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

clear = Button(window, text='clear', height=4, width=19, font=35, bg="DarkGoldenrod1",
               command=clear)

clear.pack()

# Tells Python to run the Tkinter event loop to keep the window open
window.mainloop()
