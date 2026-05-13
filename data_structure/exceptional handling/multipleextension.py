lst = [10,20,30]
d = {'a':1}
try:
    print(lst[5])
    print(d['z'])
except IndexError:
    print("List index out of range")
except KeyError:
    print("Key not found in dictionary")
