# We want to compute G_T(1/2) = E[2^-T]

# G_T(1/2) = sum_k to infty of P(T =k) 1/2^k

lam = float(input())
p = float(input())

# P(T=0) = p
# P(T=1) = (1-p)*( (choose 0 out of X) * p^X * p(X))
# P(T=2) = (1-p)*( (choose 1 out of X) * P(T=1) * p^X-1 * p(X) )
# P(T=3) = (1-p)*( (choose 2 out of X) * P(T=1)^2 * p^X-2 * p(X) )
# Etc...

