    # string functions

name = "kaVin"
newName = name.capitalize() # returns the string in Sentence case

print(name)
print(newName)

fullName = "Kavin Manoharan"
count = fullName.count("a") # returns the no of occurrences of the substring  
                         # specified as the parameter. 
count1 = fullName.count("avi")
print(count)
print(count1)

a = fullName.find("Mano")
print(a)
a = fullName.find("z")
print(a)

space = " "
iter = ("I", "am", "awesome.")
c = space.join(iter)
print(c)
hy = "-"
d = hy.join(iter)
print(d)