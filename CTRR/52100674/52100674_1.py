def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y


def inverse_modulo(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

print("Nghich dao cua {} mod {} = {}".format(10000, 7, inverse_modulo(10000,7)))
print("Nghich dao cua {} mod {} = {}".format(4, 8, inverse_modulo(4,8)))
# print(extended_gcd(7,14))
# gcd, inv_b = extended_gcd(a, m)[0:2]
# print("UCLN({}, {}) = {}".format(a, m, gcd))
