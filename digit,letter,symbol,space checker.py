import string

alph = list(string.ascii_lowercase)
digits = list(string.digits)
x = symb = space = 0

while True:

 string = input()
 digit=letter=nam=symb=space=0
 name=len(str(string))

 while nam < name:
    nam+=1
    roll =string[nam-1:nam]

    if roll in alph:
        letter+=1

    if roll in digits:
        digit+=1

    elif roll == " ":
        space+=1

    elif not roll.isalnum():

        if roll.isspace():
            space+=0

        else:
            symb+=1

 print("Letters:", letter)
 print("Digits:", digit)
 print("Symbols:", symb)
 print("spaces:", space)
