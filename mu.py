import math

n = int(input())
k = int(input())
d = []

# d_i = d[i-1]
for i in range(0, k):
    d.append(float(input()))

def bereken_kans_anders(d): 
    prob = 0
    for i in range(0,k): 
        for j in range(i,k):
            if (i != j):
                prob += d[i] * d[j]
    return prob

def bereken_kans_gelijk(d): 
    prob = 0
    for i in range(0,k): 
        prob += d[i] * d[i]
    return prob

kans_anders = bereken_kans_anders(d)
kans_gelijk = bereken_kans_gelijk(d)

def P(i,d,n):
    result = 0; 
    for getal in range(0,n):
        result += math.comb(n, getal) * (getal*kans_gelijk + (n-getal)*kans_anders)
    return result

E = 0
for i in range(1, n+1):
    E += i * P(i,d,n)

print(E)