def acronym(s):
    spaceBefore = -1
    acronym = ""
    for i in range(len(s)):
        if s[i] == " ":
            spaceBefore = i
        elif spaceBefore + 1 == i:
            acronym += s[i]
    return acronym.upper()

a = "Hello World"
print(acronym(a))
