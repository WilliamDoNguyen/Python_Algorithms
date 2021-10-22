def reverseString(str):
    newstr = ""
    for i in range(len(str), 0, -1):
        newstr += str[i - 1]
    return newstr

str = "Hello World"
print(reverseString(str))
