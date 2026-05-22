def numToRoman(number):
    number = int(number)
    txt = ""
    while number != 0:

        if number >= 1000:
            txt += "m"
            number -= 1000

        elif number >= 900:
            txt += "cm"
            number -= 900

        elif number >= 500:
            txt += "d"
            number -= 500

        elif number >= 400:
            txt += "cd"
            number -= 400

        elif number >= 100:
            txt += "c"
            number -= 100

        elif number >= 90:
            txt += "xc"
            number -= 90

        elif number >= 50:
            txt += "l"
            number -= 50

        elif number >= 40:
            txt += "xl"
            number -= 40

        elif number >= 10:
            txt += "x"
            number -= 10
            
        elif number >= 9:
            txt += "ix"
            number -= 9
            
        elif number >= 5:
            txt += "v"
            number -= 5
            
        elif number >= 4:
            txt += "iv"
            number -= 4
            
        else:
            txt += "i"
            number -= 1
            
    return txt

def romanToNum(txt):

    txt += "#"
    i = 0
    number = 0

    while True:
        if txt[i].lower() == "m":
            number += 1000
            i += 1

        elif txt[i].lower() == "c":
            if txt[i+1].lower() == "m":
                number += 900
                i += 2

            elif txt[i+1].lower() == "d":
                    number += 400
                    i += 2
                
            else:
                number += 100
                i += 1

        elif txt[i].lower() == "d":
            number += 500
            i += 1

        elif txt[i].lower() == "x":
            if txt[i+1].lower() == "c":
                number += 90
                i += 2

            elif txt[i+1].lower() == "l":
                number += 40
                i += 2

            else:
                number += 10
                i += 1
            
        elif txt[i].lower() == "l":
            number += 50
            i += 1

        elif txt[i].lower() == "i":
            if txt[i+1].lower() == "x":
                number += 9
                i += 2

            elif txt[i+1].lower() == "v":
                number += 4
                i += 2
            
            else:
                number += 1
                i +=  1

        elif txt[i].lower() == "v":
            number += 5
            i += 1

        elif txt[i] == "#":
            break

        else:
            print("")

    return number
        

def inputNumber():

    while True:
        try:
            roman = input("Enter a Roman Numeral between 0 and 4000 : ")

        except ValueError:
            print("Invalid Number. Try again\n")
            continue

        break

    return roman

def inputOperator(num1):

    while True:
        print("\nEnter Operator ")
        operator = input(f"{num1} ")

        if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator.lower() == "t":
           break

        else:
            print("Invalid Input. TRY AGAIN")
            print("You can only use '+' or '-' or '*' or '/' or 't'")
            continue

    return operator

        
def add(txtNum1,txtNum2):
    numAnswer = int(romanToNum(txtNum1)) + int(romanToNum(txtNum2))

    if numAnswer < 4000:
        txtAnswer = numToRoman(numAnswer)
        print(f"{txtNum1} + {txtNum2} = {txtAnswer}")

    else:
        print(f"Your Answer is {numAnswer} which cannot be represented in Roman Numerals")
        print("0 < Roman Numerals < 4000\n")

def sub(txtNum1,txtNum2):
    numAnswer = int(romanToNum(txtNum1)) - int(romanToNum(txtNum2))

    if numAnswer > 0 and numAnswer < 4000:
        txtAnswer = numToRoman(numAnswer)
        print(f"{txtNum1} - {txtNum2} = {txtAnswer}")

    else:
        print(f"Your Answer is {numAnswer} which cannot be represented in Roman Numerals")
        print("0 < Roman Numerals < 4000\n")

def mul(txtNum1,txtNum2):
    numAnswer = int(romanToNum(txtNum1)) * int(romanToNum(txtNum2))

    if numAnswer < 4000:
        txtAnswer = numToRoman(numAnswer)
        print(f"{txtNum1} * {txtNum2} = {txtAnswer}")

    else:
        print(f"Your Answer is {numAnswer} which cannot be represented in Roman Numerals")
        print("0 < Roman Numerals < 4000\n")

def div(txtNum1,txtNum2):
    numAnswer = round(int(romanToNum(txtNum1)) / int(romanToNum(txtNum2)))

    if numAnswer < 4000:
        txtAnswer = numToRoman(numAnswer)
        print(f"{txtNum1} / {txtNum2} = {txtAnswer}")

    else:
        print(f"Your Answer is {numAnswer} which cannot be represented in Roman Numerals")
        print("0 < Roman Numerals < 4000\n")
    



txtNum1 = inputNumber()
operator = inputOperator(txtNum1)
if operator.lower() != "t":
    txtNum2 = inputNumber()

if operator.lower() == "t":
    print(romanToNum(txtNum1))
elif operator == "+":
    add(txtNum1,txtNum2)
    
elif operator == "-":
    sub(txtNum1,txtNum2)

elif operator == "*":
    mul(txtNum1,txtNum2)
    
else:
    div(txtNum1,txtNum2)

