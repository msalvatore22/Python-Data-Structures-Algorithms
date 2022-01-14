def sum_digits(n):
    assert n>=0 and int(n) == n
    if n == 0:
        return 0
    else:
        return sum_digits(int(n/10)) + int(n)%10

print(sum_digits(12))