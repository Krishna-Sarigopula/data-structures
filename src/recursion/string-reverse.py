def reverse(input: str):
    if (len(input) == 0):
        return input
    else:
        #        return reverse(input[1:]) + input[0]
        return input[len(input)-1] + reverse(input[0:len(input)-1])


res = reverse("krishna")
print(res)
