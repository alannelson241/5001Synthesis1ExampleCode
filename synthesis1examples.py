# Alan Nelson
# 9/30/2024
# CS5001
# Synthesis 1 Example Code Fragments

# Note that deliberately broken code has been commented out



# 2.2 Assignment Operators
number = 1
print(number) # returns 1
number = 2
print(number) # returns 2, the new value assigned to number



# 2.3 Arithmetic Expressions
print("Hello" + "world") # Prints "Helloworld" with no space
print("Hello " + "world") # Prints "Hello world". Note the space in the first string after "Hello"

print("ha" * 4) # Prints "hahahaha"



# 2.4 Boolean Expressions
x = 8
x < 3 ** 3 # calculates to 8 < 9, x evaluates to True



# 2.5 Conditional Statements
if x > 5:
    print("x is more than 5")

if x > 5:
    print("x is more than 5")
else:
    print("x is less than 5")

if x > 5:
    print("x is more than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# 2.5 Solution
enemy = input("What enemy are you fighting? ")
if enemy == "fire elemental":
    print("Ice spells!")
elif enemy == "ice elemental":
    print("Fire spells!")
else:
    print("Shock spells!")



# 2.6 Logical Operators
a = True
b = True
c = False

a and b # True and True, evaluates to True
a and c # True and False, evaluates to False
a or b # True or True, evaluates to True
b or c # True or False, evaluates to True
not a # negates True, evaluates to False
not c # negates False, evaluates to True

if a == 1 or 2 or 3:
    print("this doesn't work right")



# 2.7 Tracing and Debugging
first_number = int(input("Enter a number. "))
second_number = int(input("Enter another number. "))

# sum, difference, product, and quotient of two numbers
print(first_number + second_number)
print(first_number - second_number)
#print(first_number * second_nubmer)
print(first_number / second_number)

# 2.7 Exercise
strength_mod = (int(input("Enter your strength score. ")) - 10) // 2
dexterity_mod = (int(input("Enter your dexterity score. ")) - 10) / 2
constitution_mod = (int(input("Enter your constitution score. ")) - 10) // 2
intelligence_mod = (int(input("Enter your intelligence score. ")) - 10) // 2
wisdom_mod = (int(input("Enter your wisdom score. ")) - 10) // 2
#charisma_mod = (itn(input("Enter your charisma score. ")) - 10) // 2

def main():
    print(strength_mod)
    print(dexterity_mod)
    print(constitution_mod)
    print(intelligence_mod)
    print(wisdom_mod)
    #print(charisma_mod)

main()



# 3.1 Functions
print("Hello world")
input("What is your name? ")
int("5") # returns 5
str(20) # returns "20"
float("10") # returns 10.0

#from module import function # to import a specific function from a module
#import module # to import the entire module into Python

def function():
    print("code block goes here")

def party_time():
    '''Function: party_time
    Parameter: none
    Return: string "Party time!"
    '''
    return "Party time!"

def hello_world():
    print("Hello world")
hello_world() # prints "Hello world"

# 3.1 Solution
def greeter():
    '''Function: greeter
    Parameter: none
    Return: none
    '''
    name = input("What is your name? ")
    print("Hello, " + name + "!")
greeter()

def buff_combo():
    '''Function: buff_combo
    parameter: none
    Return: none
    '''
    print("I cast Antivirus Armor!")
    print("I cast Stopwatch Start-Watch!")
    time = int(input("What time is it? "))
    if time < 12:
        print("I cast Cappuccino Quick-Charge!")
    else:
        print("I cast Cloak of Incognito!")

buff_combo()



# 3.2 Parameters
def square_a_number(x): # x is the name of our parameter, can be used inside the function
    print(x ** 2)
square_a_number(2) # calculates 2 ** 2 = 4; prints 4
square_a_number(5) # calculates 5 ** 2 = 25; prints 25

def multiply(x, y): # x and y are both parameters, need to assign a value for both
    print(x * y)
multiply(2, 3) # calculates 2 * 3; prints 6
multiply(8, 10) # calculates 8 * 10; prints 80

apple = 'red'
banana = 'yellow'

def fruit_colors(fruit_one, fruit_two):
    print("There is a " + fruit_one + " fruit and a " + fruit_two + " fruit in the bowl.")
fruit_colors(apple, banana) # prints "There is a red fruit and a yellow fruit in the bowl."

# 3.2 Solution
def spellstrike(spell, weapon):
    print("Spellstrike! " + spell + " cast through the " + weapon + "!!!")
spellstrike("Ice Punch", "shortsword")



# 3.3 Scope
'''x = 1
def add_10(a):
    plus_ten = a + 10
    print(plus_ten)
add_10(x) # prints 11'''

x = 1
def add_10(a):
    global x
    plus_ten = a + 10
    print(plus_ten)
add_10(x) # prints 11

# 3.3 Exercise
'''off_guard = input("Is the enemy off guard? yes/no ")
def sneak_attack():
    if off_guard == "yes":
        print("Sneak attack! Massive damage!")
    else:
        print("Need to flank! Moving into position.")
        off_guard == "yes"
sneak_attack()'''



# 3.4 Return Statements
x = 5
def add_one(number):
    y = number + 1
    return y
print(add_one(x)) # prints 6; the value of y is passed out of the function in the return statement

x = 5
def add_one(number):
    y = number + 1
    return y
x = add_one(x) # reassigns x to equal the value returned by add_one
print(x) # prints 6

# 3.4 Exercise
'''door_kicked = False
def kick_down_door(kicked):
    if kicked == False:
        return "GRRRAGH! KICK IT DOWN!"
        kicked = True
        return kicked
    else:
        return "HA! TAKE THAT DOOR! I'M GOING IN NOW!"
    
print(kick_down_door(door_kicked)) # why
print(kick_down_door(door_kicked)) # won't
print(kick_down_door(door_kicked)) # you
print(kick_down_door(door_kicked)) # kick'''



# 3.5 Testing Functions
def side_finder():
    a = float(input("Enter the length of a triangle's first side: "))
    b = float(input("Enter the length of a triangle's second side: "))
    c = (a ** 2 + b ** 2) ** 0.5
    return c

# 3.5 Exercise
#import random # random number generation disabled to test the function manually
sneak_attack = input("Did you land a sneak attack? yes/no ")
dex_mod = 3

def attack_damage(sneak_check):
    if sneak_check == 'yes':
        #die_one = random.randint(1, 4)
        die_one = int(input("testing: enter first die value. between 1 and 4 "))
        #die_two = random.randint(1, 6)
        die_two = int(input("testing: enter second die value. between 1 and 6 "))
        #die_three = random.randint(1, 6)
        die_three = int(input("testing: enter third die value. between 1 and 6 "))
        damage = die_one + die_two + die_three + dex_mod
        return damage
    else:
        #die_one = random.randint(1, 4)
        die_one = int(input("testing: enter first die value. between 1 and 4 "))
        damage = die_one + dex_mod
        return damage
