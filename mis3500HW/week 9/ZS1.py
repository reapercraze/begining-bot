#programming activity 1
user_name = input("What is you name? ")

user_name = user_name.upper()

print("Welcome,", user_name + "!")

#programming activity 2
msg = "dude, I just biked down that mountain \
and at first I was like Whoa and then I was like Whoa"

msg = msg.capitalize()
first_whoa = True
i = 0
words = msg.split()
for word in words:
    if word[:4] == "whoa" and first_whoa:
        words[i] = words[i].lower()
        first_whoa = False
    elif word[:4] == "whoa" and not first_whoa:
        words[i] = words[i].upper()
    else:
        pass
    i += 1

new_msg = ""
for word in words:
    new_msg += " " + word

new_msg += "!"

print(new_msg)