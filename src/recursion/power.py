def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp + 1)

    return base * power(base, exp - 1)


res = power(16, -1)
print(res)
