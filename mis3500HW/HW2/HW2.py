#section 2.3
grade = input("Whats your grade? ")
grade = eval(grade)
if grade >= 90:
    print("Congradulations! Your grade of",grade,"earns you an A in this course.")

#section 2.4 
value = 27.5 + 2
print("The value is", value)
value = 27.5 - 2 
print("The value is", value)
value = 27.5 * 2
print("The value is", value)
value = 27.5 / 2
print("The value is", value)
value = 27.5 // 2
print("The value is", value)
value = 27.5 ** 2
print("The value is", value)

#2.5

r = 2
pi = 3.14159
diameter = 2 * r
print("diameter: ", diameter,)
circumfrence = 2 * pi * r
print("circumfrence: ",circumfrence,)
area = pi * r **2
print("area: ", area,)

#2.6

odd = int(input("Type a number. "))
even = odd % 2
if even == 1:
    print(odd,"is an odd number")
if even == 0:
    print(odd,"is an even number")
    
#2.7

four = 1024 % 4
if four > 0:
    print("4 is not a multiple of 1024")
if four == 0:
    print("4 is a multiple of 1024")
two = 10 % 2
if two > 0:
    print("2 is not a multiple of 10")
if two == 0:
    print("2 is a multiple of 10")

#2.8

print("number\tsquare\tcube")
x=0
two_x = x**(2)
three = x**(3)
print(x,"\t",two_x,"\t",three,)
x=1
two_x = x**(2)
three = x**(3)
print(x,"\t",two_x,"\t",three,)
x=2
two_x = x**(2)
three = x**(3)
print(x,"\t",two_x,"\t",three,)
x=3
two_x = x**(2)
three = x**(3)
print(x,"\t",two_x,"\t",three,)
x=4
two_x = x**(2)
three = x**(3)
print(x,"\t",two_x,"\t",three,)
x=5
two_x = x**(2)
three = x**(3)
print(x,"\t",two_x,"\t",three,)