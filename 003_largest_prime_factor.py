# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math
number = 600851475143
factors = []
for i in range(1, int(math.sqrt(number))):
    if number % i == 0:
        factors.append(i)

for i in factors:
    for j in range(2, int(math.sqrt(i))):
        if i % j == 0:
            break
    else:
        print(i)
