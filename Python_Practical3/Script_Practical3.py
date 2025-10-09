mylist = ["a", "list", "can", "contain", "strings", "and", "numbers", 2]
# You can double check if it's a list
print(type(mylist).__name__)

# print your list
print(mylist)

# print the first item in your list
print(mylist[0])

Looplist = ["WoW", "Such", "a", "cool", "Stop", "List", "bro"]
for index, item in enumerate (Looplist, start=1):
    print(index, item)
    if index == 5:
        break
print("Loop is done")
