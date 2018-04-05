import numpy as np

# Compute powers of two using dynamic programming to store in an array
def pow(n):
    P = np.zeros((n+1))
    for k in range(0,n+1):
        if k == 0:
            P[k] = 1
        else:
            P[k] = P[k-1] + P[k-1]
    return P[n]

# Removed extra if check each iteration
def pow2(n):
    P = [0 for x in range(0,n+1)] # List comprehension instead of numpy array
    P[0] = 1
    for k in range(1,n+1):
        P[k] = P[k-1] + P[k-1]
    return P[n]

print(pow(16))
print(pow2(16))