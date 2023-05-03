import statistics
scores = [6,7,2,6,3,5,5,5,2,5,6,1,2]
a = statistics.mean(scores)
print(a)
b = statistics.median(scores)
print(b)
c = statistics.mode(scores)
print(c)
d = statistics.median_low(scores)
print(d)
e = statistics.median_high(scores)
print(e)
