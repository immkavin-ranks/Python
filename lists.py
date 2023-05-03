    # lists.py
list1  = [2,4,5,6,3,7,3]

a = list1[2]
print(a)

b = list1[1:3]
print(b)

print(list1[:])
print(list1[:4])
print(list1[3:])

list1[0] = 1
print(list1[:])
list1.append(100) # we can use loop to add more using append function 
print(list1[:])

del list1[3]        # deleting data in lists        # del statement
print(list1[:])
list1.remove(100)   # specifying the element ->     # remove function
print(list1)        # :)
