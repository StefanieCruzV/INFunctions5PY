# # 1 -> 5
def number_of_food_groups():
    return 5

print(number_of_food_groups())
print("----------------------------------")

# #2-> error cause don know that function
# def number_of_military_branches():
#     return 5

# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#print("----------------------------------")

# # 3-> 5
def number_of_books_on_hold():
    return 5
    return 10

print(number_of_books_on_hold())
print("----------------------------------")

# # 4-> 5
def number_of_fingers():
    return 5
    print(10)

print(number_of_fingers())
print("----------------------------------")

# # 5-> 5 / undefined
def number_of_great_lakes():
    print(5)

x = number_of_great_lakes()
print(x)
print("----------------------------------")

# # 6 -> 3 / 5/ undefine
def add(b, c):
    print(b+c)


#print(add(1, 2) + add(2, 3))
print("----------------------------------")


# # 7 -> 25
def concatenate(b, c):
    return str(b)+str(c)


print(concatenate(2, 5))
print("----------------------------------")

# # 8 -> 100 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(number_of_oceans_or_fingers_or_continents())
print("----------------------------------")

# # 9 -> 7 /14 / 7 /21
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) + number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))

print("----------------------------------")

# # 10 ->8
def addition(b, c):
    return b+c
    return 10


print(addition(3, 5))
print("----------------------------------")

# # 11 -> 500 /500/ 300 /500
b = 500
print(b)


def foobar():
    b = 300
    print(b)


print(b)
foobar()
print(b)

print("----------------------------------")

# # 12-> 500/500/300/300         x 500/500/300/300
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
foobar()
print(b)

print("----------------------------------")
# # 13 -> 500/500/300/300
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
b = foobar()
print(b)
print("----------------------------------")

# # 14->1/3/2
def foo():
    print(1)
    bar()
    print(2)


def bar():
    print(3)


foo()
print("----------------------------------")

# # 15-> 1/3/5/10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10


def bar():
    print(3)
    return 5


y = foo()
print(y)

print("----------------------------------")
