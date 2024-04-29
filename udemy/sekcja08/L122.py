import datetime
import time
import random

start_time=time.perf_counter()
time.sleep(random.randint(1,5))
end_time=time.perf_counter()

if (end_time-start_time)>3:
    print("duzo czasu")
else:
    print("krótki czas")
