from datetime import datetime 

birth_year = input("What year were you born? ")

if birth_year < 1980:
    print("Your are Gen X")
elif birth_year < 1996:
    print("Your are a Millennials")
elif birth_year <