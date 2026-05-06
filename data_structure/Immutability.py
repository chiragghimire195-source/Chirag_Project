
t = (5, 10, 15, 20)
print("Original tuple:", t)

t_list = list(t)

t_list[1] = 99

t = tuple(t_list)

print("Modified tuple:", t)