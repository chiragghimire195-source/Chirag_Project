try:
    num = int (input("enter a number:"))
    try:
        result = 100 / num
        print(result)
    except ZeroDivisionError:
        print("cannot divisible by zero")
    except ValueError:
        print("please enter a valid integer")
        