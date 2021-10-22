def gcf(a, b):
    if(a > b):
        c = a % b
        if(c == 0):
            return b
        else:
            return gcf(b, c)
    elif(a < b):
        c = b % a
        if(c == 0):
            return a
        else:
            return gcf(a,c)
    else:
        return a

aGCF = print(gcf(123456, 987654))
bGCF = print(gcf(12, 15))
