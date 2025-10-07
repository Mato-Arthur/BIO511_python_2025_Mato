Integer = 1
Float = 4.20
Boolean = True
Letter = "Amanda"
List = (1 , 2 , 3)
Set = {"blue", "green", "red", "yellow"}
dictionary = {"Name": "Mato", "Age": "24"}
Range = range(0, 5)

print(type(Integer), Integer)
if Integer > 0:
    print("This is a positive integer")
    if Integer == 0:
        print("This is zero")
else: print("This is a negative integer")
 

print(type(Float), Float)
print(type(Boolean), Boolean)
print(type(Letter), Letter)

print(type(List), List)
var1 = type(List).__name__
if type(List) == list or type(List) == tuple or type(List) == range:
    if len(List) == 0: 
        print(f"This is an empty {var1}")
    elif len(List) == 1:
        print(f"This is a {var1} with one element")
    else: print(f"This is a {var1} with multiple elements")
else: print("Wrong datatype for Task")

print(type(Set), Set)
print(type(dictionary), dictionary)
print(type(Range), Range)
