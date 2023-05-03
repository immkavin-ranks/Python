import statistics
grades = [70,90,50,85,65,83,94]     # positive
grades1 = [80,80,80,80,80,80,80]        # zero
grades_mean = statistics.mean(grades1)
print('Variance of data is: ', statistics.variance(grades1, grades_mean))
