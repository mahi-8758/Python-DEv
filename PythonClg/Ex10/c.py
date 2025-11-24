from math import gcd as math_gcd

def gcd(a, b): return a if b == 0 else gcd(b, a % b)

def lcm(a, b): return (a * b) // gcd(a, b)

print("=" * 50)
print("GCD AND LCM")
print("=" * 50)

pairs = [(12, 8), (18, 24), (15, 25), (48, 18)]

for a, b in pairs:
    print(f"\nNumbers: {a}, {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")