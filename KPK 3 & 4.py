def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = 3
b = 4
print("KPK dari", a, "dan", b, "adalah", lcm(a, b))
