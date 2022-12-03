def reverse(input: str):
    if (len(input) == 0):
        return input
    else:
        return reverse(input[1:]) + input[0]

res = reverse("krishna")
print(res)
