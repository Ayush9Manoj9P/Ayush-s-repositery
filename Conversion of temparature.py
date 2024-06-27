why = c = f = k = 0
scale = ['c', 'f', 'k']  # the scales
er = "Error: Invalid scale entered."

def y_notin_scale(y):
    if y not in scale:
        return True

def x_notin_scale(x):
    if x not in scale:
        return True

def is_num(num):
    return num.isdigit()

def scales(x, y, num):
    if x == "c":
        if y == "f":
            print(f"{num}°C is equal to {(int(num) * 9/5) + 32}°F")
        elif y == "k":
            print(f"{num}°C is equal to {int(num) + 273.15}K")

    elif x == "f":
        if y == "c":
            print(f"{num}°F is equal to {(int(num) - 32) * 5/9}°C")
        elif y == "k":
            print(f"{num}°F is equal to {(int(num) - 32) * 5/9 + 273.15}K")

    elif x == "k":
        if y == "c":
            print(f"{num}K is equal to {int(num) - 273.15}°C")
        elif y == "f":
            print(f"{num}K is equal to {(int(num) * 9/5) - 459.67}°F")


def checks():
    x = input("Enter the initial scale (c, f, k): ").lower()
    if x_notin_scale(x):  # if x is not in scale
        print(er)
    else:
        y = input("Enter the target scale (c, f, k): ").lower()
        if y_notin_scale(y):
            print(er)
        elif y == x:
            print("You entered the same scale!")
        else:
            num = input(f"Enter the temperature in {x.upper()} to convert: ")  # gets the number to convert to another scale
            if is_num(num):
                scales(x, y, num)
            else:
                print("Error: Not a valid number entered.")


def main():
    checks()

while True:
    main()
