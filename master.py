
import numpy as np
import time

# for find start time
start_time = time.time()

# Matrix X * X column and rows
x = 5
# for find how many times turns while loops
counter_genel = 0
whlcont = True

while whlcont:
    a = np.random.random((x, x))
    b = np.random.random((x, x))
    counter_genel += 1
    # to check if all diaganal items provides the condition
    counter = 0
    for i in range(x):
        for j in range(x):
            if i == j:
                sub = np.subtract(a, b)
                if -0.1 <= sub[i, j] and sub[i, j] >= 0.1:
                    counter += 1
                    if counter == x:
                        print(sub)
                        print("\nHow many times turn :", counter_genel)
                        end_time = time.time()
                        current_time = str(end_time-start_time)
                        print("\nFound in {:.4f} seconds".format(
                            float(current_time)))

                        whlcont = False
