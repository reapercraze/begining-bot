#Programming activity 1
# name = input("What is your name? ")
# fav_color = input("What is your favorite color? ")

# with open("accounts.txt", "w") as accounts:
#     accounts.write(name + "'s favorite color is " + fav_color)
    
#Programming activity 2
def add(num1, num2):
   return  num1 + num2
    
print(add(15,25))

#programming activity 3 
def multiply(num1, num2):
    tot = 0
    for i in range(num2):
        tot = add(tot, num1)
    return tot
    
print(multiply(12,24))

#Proframming activity 4
def exponent(num1, num2):
    tot = 1
    for i in range(num2):
        tot = multiply(tot, num1)
    return tot
    
print(exponent(3,5))