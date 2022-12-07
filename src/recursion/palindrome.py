def palindrome(n, temp):
    if n < 1:
        return temp

    temp = (temp * 10) + (n % 10)
    return palindrome(int(n/10), temp)


res = palindrome(2002, 0)
print(res == 2002)
