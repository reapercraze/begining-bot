fav_things = ["sports", "video games", "steak", "dogs"]

def print_item(lst, idx):
    if idx == (len(lst)):
        return
    print(lst[idx])
    print_item(lst, idx + 1)
    

print_item(fav_things, 0)

