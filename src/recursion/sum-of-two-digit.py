def sumofdigits(n):
    if n < 1:
        return n

    return int(n % 10) + sumofdigits(int(n/10))


res = sumofdigits(111)
print(res)
