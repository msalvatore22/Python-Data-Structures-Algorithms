def convert_to_binary(n):
    assert int(n) == n
    if n == 0:
        return 0
    else:
        return n%2 + 10 * convert_to_binary(int(n/2))

print(convert_to_binary(10))