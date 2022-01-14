def power(base, exp):
    assert base>0 and int(base)==base and exp>0 and int(exp) == exp
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp-1)


print(power(3,3))