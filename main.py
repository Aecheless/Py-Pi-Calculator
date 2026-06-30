from decimal import Decimal, getcontext

def arctan_inv(b: Decimal, eps: Decimal):
    x = 1 / b
    x2 = x * x
    res = x
    term = x
    sign = -1
    denom = 3
    while abs(term / denom) > eps:
        term *= x2
        res += sign * term / denom
        sign *= -1
        denom += 2
    return res

def machin(pi_digits: int):
    prec = pi_digits + 20
    getcontext().prec = prec
    eps = Decimal("10") ** (-prec)
    
    a1, b1 = Decimal(4), Decimal(5)
    a2, b2 = Decimal(-1), Decimal(239)
    
    s = a1 * arctan_inv(b1, eps) + a2 * arctan_inv(b2, eps)
    pi = 4 * s
    return +pi

if __name__ == "__main__":
    pi = machin(10000) #求值的位数
    print(pi)
