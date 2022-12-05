def decimalToBinary(n):
    if n < 1:
        return 0

    return n % 2 + 10 * decimalToBinary(int(n/2))


res = decimalToBinary(13)
print(res)
