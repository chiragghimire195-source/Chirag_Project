
numbers = [3, 8, 15, 22, 7, 44, 6, 11, 19, 30]

even_count = 0
odd_count = 0


for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)