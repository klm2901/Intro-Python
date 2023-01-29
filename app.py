##hello world
print("Hello World")
#variables and types
mystring = "hello"
myfloat = 10.0
myint = 20
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    #Lists
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

    ##basic operartors

    #operators for maths

number = 1 + 2 * 3 / 4.0
print(number)

#pyhton follows the order of operations
#modulu operator gets the remainder of the division
remainder = 11 % 3
print(remainder)

#using multipication symbol twice makes indices
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#you can add strigns together using plus sign

helloworld = "hello" + " " + "world"
print(helloworld)

#string formating
#tuple is a fixed size list

name = "John"
print("Hello, %s!" % name)

##String argument specifiers are %s
##to use more than 1 arguement specifier you must use extra brackets eg
name = "John"
age = 23
print("%s is %d years old." % (name, age))
## you can make objects that arent strings usinf the same method eg
mylist = [1,2,3]
print("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %s"

print(format_string % data) 

##Basic string operations
astring = "Hello world!"
astring2 = 'Hello world!'
##strings are sentences/text define them with quotes
astring = "Hello world!"
astring2 = 'Hello world!'
##yoh should try to use double quotes as it causes problems if you dont.
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))
#this counts lenth of string

print(astring.index("o"))
#this finds the first instance of the characters in a string

print(astring.count("l"))
#this counts the number of times the hcaracters appear

print(astring[3:7])
#this begins to print the string from the 3rd character untill 7th however not including 7

print(astring[3:7])
print(astring[3:7:4])
#you can print from the 3rd and 7th however u can skip a character start stop step

