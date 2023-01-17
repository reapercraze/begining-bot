#3.4

for r in range(2):
    for c in range(7):
        print('@', end="")
    print()

#3.9

num = input("type a 7-10 digit number. ")
for space in num:
    print(space)
print()

#3.11

total_gallons = 0
total_miles = 0
gallons = 0
gallons = eval(input("How many gallons did you use? (Enter -1 to end) "))

while gallons != -1:
    total_gallons += gallons
    miles = eval(input("How many miles did you drive? "))
    total_miles += miles
    mpg = miles / gallons
    print("The miles per gallon was", mpg)
    gallons = eval(input("How many gallons did you use? (Enter -1 to end) "))

if total_gallons != 0:
    total_mpg = total_miles / total_gallons
    print("The overal miles per gallon was", total_mpg)
else:
    print("No gallons were entered.")
    
#3.12

print()

palidrom = ""
user_input = input("type in a number ")
for i in range(len(user_input)-1,-1,-1):
    palidrom += user_input[i]
if palidrom == user_input:
    print(user_input, "is a palidrom")
else:
    print(user_input, "is not a palidrom")
    
#3.14
#120 terms before you get 3.14. 629 terms before you start seeing 3.14 twice. 1689 terms to get 3.141

pi = 0
n = 1
for x in range(1,5001,2):
    if n % 2 == 1:
        pi += (4/x)
    else:
        pi -= (4/x)
    n += 1
    print("pi is approximated to ", pi)
    print(n)
    
