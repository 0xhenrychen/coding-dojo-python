num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # data types > primitive > boolean
string = 'Hello World' # data types > primitive > strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # data types > composite > list > initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # data types > composite > dictionary > initialize
fruit = ('blueberry', 'strawberry', 'banana') # data types > composite > tuples > initialize
print(type(fruit)) # type check
print(pizza_toppings[1]) # data types > composite > list > access value
pizza_toppings.append('Mushrooms') # data types > composite > list > add value
print(person['name']) # data types > composite > dictionary > access value
person['name'] = 'George' # data types > composite > dictionary > change value
person['eye_color'] = 'blue' # data types > composite > dictionary > add value
print(fruit[2]) # data types > composite > tuple > access value

if num1 > 45: # conditional > if
    print("It's greater") # log statement
else: # conditional > else
    print("It's lower") # log statement

if len(string) < 5: # len check, conditional > if
    print("It's a short word!") # log statement
elif len(string) > 15: # len check, conditional > else if
    print("It's a long word!") # log statement
else: # conditional > else
    print("Just right!") # log statement

for x in range(5): # for loop > start
    print(x) # log statement
for x in range(2,5):# for loop > start
    print(x) # log statement
for x in range(2,10,3):
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # while loop > start
    print(x) # log statement
    x += 1 # white loop > increment

pizza_toppings.pop() # data types > composite > list > delete value
pizza_toppings.pop(1) # data types > composite > list > delete value

print(person) # log statement
person.pop('eye_color') # data types > composite > dictionary > delete value
print(person) # log statement

for topping in pizza_toppings: # for loop > start
    if topping == 'Pepperoni': # conditional > if
        continue # for loop > continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional > if
        break # for loop > break

def print_hello_ten_times(): # function > parameter
    for num in range(10): # for loop > start
        print('Hello') # log statement

print_hello_ten_times() # function > argument

def print_hello_x_times(x): # function > parameter
    for num in range(x): # for loop > start
        print('Hello') # log statement

print_hello_x_times(4) # function > argument

def print_hello_x_or_ten_times(x = 10): # function > parameter
    for num in range(x): # for loop > start
        print('Hello') # log statement

print_hello_x_or_ten_times() # function > argument
print_hello_x_or_ten_times(4) # function > argument


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 # variable declaration
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team' 
# print(pizza_toppings[7]) # IndexError: list index out of range
# print(boolean)
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'