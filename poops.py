why = c = f = k = 0
scale = ['c', 'f', 'k']  # the scales
er = "error"

def y_notin_scale(y):
    if y not in scale:
        return

def x_notin_scale(x):
    if x not in scale:
        return 1

def is_num(num):
    return num.isdigit()

def scales(x, y, num):
    if x == "c":
        if y == "f":
            print((int(num) * 9/5) + 32)
        if y == "k":
            print(int(num) + 273.15)

    if x == "f":
        if y == "c":
            print((int(num) - 32) * 5/9)
        if y == "k":
            print((int(num) - 32) * 5/9 + 273.15)

    if x == "k":
        if y == "c":
            print(int(num) - 273.15)
        if y == "f":
            print((int(num) * 9/5) - 459.67)


def checks():
    x = input("c?, f?, k?")
    if x_notin_scale(x) == 1:  # if x is not in scale
        print(er)
    else:
        y = input("c?, f?, k?")
        if y_notin_scale(y) == 1:
            print(er)
        if y == x:
            print("same scale!!")
        else:
            num = input("num:")  # gets the number to convert to another scale
            if is_num(num) == True:
                scales(x, y, num)
            else:
                print("not num")

def main():
    checks()

while True:
    main()
