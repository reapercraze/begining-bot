#3.4

for r in range(2):
    for c in range(7):
        print('@', end="")
    print()

#3.9

num = input("type a 5 digit number. ")
for space in num:
    print(space, end="   ")
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
    

if total_gallons != 0:
    total_mpg = total_miles / total_gallons
    print("The overal miles per gallon was", total_mpg)
else:
    print("No gallons were entered.")