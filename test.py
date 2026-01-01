a = [1]
b = True == [1]
c = False == [1]

if a:
    print(a)
print(b)
print(c)
print(a or c)


# результат:
# [1]
# False
# False
# [1]
