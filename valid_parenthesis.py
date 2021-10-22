def parensValid(s):
    parensCounter = 0
    bracecounter = 0
    for i in range(len(s)):
        if s[i] == "(":
            parensCounter += 1
        elif s[i] == ")":
            parensCounter -= 1
        elif s[i] == "[":
            bracecounter += 1
        elif s[i] == "]":
            bracecounter -= 1
    if parensCounter == 0 or bracecounter == 0:
        return True
    return False

a = "Y(3(p)[p(3)r)]s"
print(parensValid(a))
