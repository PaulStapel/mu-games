import sys

sys.set_int_max_str_digits(1_000_000)

k = int(input())
Mk = int(input())

def back_step0(Ml):
    return (Ml - 7) / 4

def back_step1(Ml):
    return (Ml - 2) / 9

def eval(Ml):
    Ml_old = back_step0(Ml)
    if (Ml_old % 1) == 0:
        return Ml_old
    else:
        Ml_old = back_step1(Ml)
        return Ml_old

Ml = Mk
for i in range(k):
    Ml = eval(Ml)

print(int(Ml))