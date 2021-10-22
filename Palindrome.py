def palindrome(a):
    length = len(a)
    temp_one = ''
    for x in range(length-1, -1, -1):
        temp_one += a[x]
    if temp_one == a:
        return True
    else:
        return False

a = 'tacocat'
b = 'Hello World'
print(palindrome(a))
print(palindrome(b))


# compares front and back
def isPal2(stringInput):
    for i in range(0, len(stringInput)//2, 1):      # // floor division
        if stringInput[i] != stringInput[len(stringInput)-1-i]:
            return False
    return True

a = 'tacocat'
b = 'Hello World'
print(isPal2(a))
print(isPal2(b))

# challenge 2: deal with punctuation and spaces
def pal(_str):
    punc = {
        "space":" ",
        "exclaim":"!",
        "period":"."
    }
    for key, value in punc.items():
        _str = _str.replace(value,"")
    _str = _str.lower()
    # _str = _str.replace(punc[value],"")
    for i in range (round(len(_str)/2)):
        if _str[i] != _str[len(_str)-1-i]:
            return False
    return True

print(pal("Race .!Car"))
