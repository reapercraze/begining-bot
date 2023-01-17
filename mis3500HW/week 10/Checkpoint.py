#8.7
row = "row row row your boat"
ct = row.count("row")
print("ct: ", ct)
where = row.index("row")
print("first row: ", where)
last = row.rindex("row")
print("last row: ", last)

#8.8
fav = "My favorite fruit is an apple"
fav = "Nevermind, " + fav
fav = fav.replace("apple", "necturine")
print(fav)

#5.12
lst = [i for i in range(2, 101, 2)]
print("even: ", lst)

#8.9
phrase = "1 2 3 4 5 6 7 8 9 10"
lst = phrase.split(" ")
print("list: ", lst)
ints = [int(i) for i in lst]
print("ints: ", ints)

#8.10
age = input("What is your age? ")
print(age.isdigit())