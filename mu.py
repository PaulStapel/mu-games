import math

n = input()
k = input()
d = []

# d_i = d[i-1]
for i in range(0, k):
    d.append(input())

def P(i,d,n):
    pass

E = 0
for i in range(1, n+1):
    E += i * P(i,d,n)

print(E)