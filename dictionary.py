#   dictionary -> data structure
#   key - value pair
dict1 = {
    'name':'kavin',
    'age':21,
    'hobby':'drawing'
}
#   unordered data structures

#   accessing
print(dict1['name'])
print(dict1)

#   updating
dict1['hobby'] = 'music'
print(dict1)

#   to add a new key-value pair
dict1['degree'] = 'BCA'
print(dict1)

#   deleting data in dictionary
del dict1['hobby']
print(dict1)

#   remove all the items and empty the dictionary
dict1.clear()
print(dict1)

#   to remove the entire dictionary
del dict1

