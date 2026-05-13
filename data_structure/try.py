try :
    num1 = input("Enter the number")
    num2 = input("Enter the number")
    div = int(num1)/int(num2)
    print(div)
except ZeroDivisibleError:
    print("Cannot divide by 0")
except ValueError:
    print("The value to be integer")
except Exception as e:
    print(e)
else:
    print("Hello the blocked run")
finally:
    print("program executed succesfully")   
             