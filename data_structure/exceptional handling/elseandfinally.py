try:
    num = (input("Enter a number"))
    print(num)
except ValueError:
    print("invalid input")
else:
    print("conversion successful")
finally:
    print("program ended successfully")
    