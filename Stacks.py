arr = []
newArr = []
arr.append(20)
arr.append(-5)
arr.append(600)
arr.append(13)
for x in range(len(arr)-1, -1, -1):
    newArr.append(arr[x])
newArr.pop()
print(newArr[0])
print(len(newArr))
print(arr)
print(newArr)

def isIn(array_input, findValue):
    for i in range(len(array_input)):
        if array_input[i] == findValue:
            print("True")
            return True
    print("False")
    return False

isIn(newArr, 27)
isIn(newArr, -5)

def emptyArray(input):
    if len(input) == 0:
        print("Array is empty")
        return False
    else:
        print("Array is not empty")
        return True

newNew = []

emptyArray(newArr)
emptyArray(newNew)

class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def topper(self, valueInput):
        newNode = Node(valueInput)
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        return self

    def pop(self):
        temp = self.top.value
        self.top = self.top.next
        return temp

    def Top(self):
        if self.top != None:
            temp = self.top.value
            print(temp)
            return self
        else:
            print("nothing in queue")
            return None

    def display(self):
        runner = self.top
        result = ""
        while runner != None:
            result += f"{runner.value}-->"
            runner = runner.next
        print(result)
        return self

    def size(self):
        runner = self.top
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        print(count)
        return count

    def contains(self, valueToFind):
        runner = self.top
        while runner != None:
            if runner.value == valueToFind:
                print("I gotchu")
                return True
            runner = runner.next
        print("Nah Fam")
        return False

    def isEmpty(self):
        if self.top == None:
            print("There's nothing there!")
            return True
        else:
            print("Nope, not empty.")
            return False

stack_one = Stack()
stack_two = Stack()
stack_one.topper(3).topper(6).topper(9).display()
stack_one.Top().size()
stack_one.contains(6)
stack_one.contains(-1)
stack_one.isEmpty()
stack_two.isEmpty()
