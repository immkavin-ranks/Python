import time
epoch_time = time.time()
    #   returns the number of seconds that have passed since the epoch.
    #   returns a floating-point number.
local_time = time.ctime(epoch_time)
print('Local time is:', local_time)

