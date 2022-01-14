def greatest_divisor(a, b):
    assert int(a) == a and int(b) == b
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b==0:
        return a
    else:
        return greatest_divisor(b, a % b)

print(greatest_divisor(48,18))        