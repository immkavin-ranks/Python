import random
numberList = [151,251,351,451,551]
print(random.choices(numberList,weights=(10,20,30,40,50),k=5))
