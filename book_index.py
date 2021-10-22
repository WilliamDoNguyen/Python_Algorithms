#My attempt (only works for sequences that are in 3's)

def bookindex(arr):
    newArr = []
    for i in range(len(arr)-1):
        if arr[i] + 1 == arr[i+1]:
            print(i)
            newArr.append(arr[i])
            newArr.append("-")
            print(newArr)
            print(arr[i])
            if newArr[i+1] != "-" and arr[i + 1] == arr[i] + 1 and arr[i-1] == arr[i] - 1:
                newArr.pop()
                newArr.pop()
        else:
            newArr.append(arr[i])
            newArr.append(",")
    newArr.pop()
    return newArr

arr = [1,2,3,5,8,9,10,13,15]
result = ' '.join(map(str, bookindex(arr)))
print(result)

Correct way

def bookIndex(arr):
    # Assume the array is sorted, but just in case...
    arr.sort()
    result = ""
    in_sequence = False
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]-1:
            if not in_sequence:
                # this adds the first number in the sequence
                result += str(arr[i]) + "-"
            in_sequence = True
        else:
            # add a non-sequential number or the last number in a sequence
            result += f"{str(arr[i])},"
            in_sequence = False
    result += str(arr[i+1])
    return result

print(bookIndex([1,2,3,5,8,9,10,13,15]))
print(bookIndex([1,2,3,4,7,10,11,12,13]))
print(bookIndex([1,12,3,7,10,4,2,13,11]))
