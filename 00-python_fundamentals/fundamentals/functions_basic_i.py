# #1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

# # Prints "5".


# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# # Returns an error as number_of_days_in_a_week_silicon_or_triangle_sides() isn't defined.


# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

# # Prints "5".


# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

# # Prints "5".


# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)

# # Prints "5" from within the function but nothing from the print(x) statement.


# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# # add(1,2) = print(3)
# # add(2,3) = print(5)
# # Prints "3" and "5" from within the function but error from the print(add(1,2) + add(2,3)) statement as you can't print a "none" type.


# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))

# # concatenate(2,5) = 25
# # Prints "25".


# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())

# # Function prints "100". Returns 10 as 100 > 5.
# #Prints "10".


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# # Prints "7", "14", "21".


# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))

# # Prints "8".


# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

# # Prints "500", "500", "300" (from within the foobar function), "500".


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)

# # Prints "500", "500", "300" (from within the foobar function), "500".


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)

# # Prints "500", "500", "300" (from within the foobar function), "300".


# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()

# # Prints "1" (from within the foo function), prints "3" (from within the bar function), prints "2" (from within the foo function).


#15
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

# Prints "1" (from within the foo function), prints "3" (from within the bar function), prints "5" (from the return of the bar function), prints "10" (from the return of the foo function).