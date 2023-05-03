import random
print('Random number 1=> ', random.random())
print('Random number 2=> ', random.random())

print('Random number 1=> ', random.randint(1, 10))
print('Random number 2=> ', random.randint(1, 10))

print(random.randrange(0, 10)) # returns a random integer between 0 and 9 inclusive
print(random.randrange(0, 10, 2)) # returns a random even integer between 0 and 8 inclusive