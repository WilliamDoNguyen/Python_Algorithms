class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def back(self, valueInput):
        if self.head == None:
            self.head = Node(valueInput)
            self.tail = Node(valueInput)
            return self
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = Node(valueInput)
            return self

    def dequeue(self):
        if self.head != None:
            temp = self.head.value
            self.head = self.head.next
            return self
        else:
            print("nothing in queue")
            return None

    def Top(self):
        if self.head != None:
            temp = self.head.value
            print(temp)
            return self
        else:
            print("nothing in queue")
            return None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def contains(self, valueToFind):
        runner = self.head
        while runner != None:
            if runner.value == valueToFind:
                return True
            runner = runner.next

        return False

    def size(self):
        runner = self.head
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        return count

    def display(self):
        runner = self.head
        output = ""
        while runner != None:
            output += f"{runner.value} -->"
            runner=runner.next
        print(output)
        return self

    def palindrome(self):
        runner = self.head
        tail = self.tail
        emptyarray1 = []
        emptyarray2 = []

        while runner.next != None:  # since we don't know where the end of the iteration will be, we use a while loop because a while loop will end itself, as opposed to a for loop where we tell it where we want it to stop.
            emptyarray1.append(runner.value)
            runner = runner.next
        emptyarray1.append(tail.value)
        print(emptyarray1)

        for i in range(len(emptyarray1) -1, -1, -1) :  # range = start: at the end of the array, stop at the beginning of the array, and decrement by 1.
            emptyarray2.append(emptyarray1[i])
        print(emptyarray2)

        if emptyarray1 == emptyarray2:
            return True
        else:
            return False

line = Queue()
line2 = Queue()

line.back(50).back(-2).back(3).back(4).display().isQueuePal()
line2.back(1).back(2).back(3).back(2).back(1).display().isQueuePal()




# line.dequeue().display()
# line.Top()

# print(line.isEmpty())

# print(line.contains(3))

# print(line.size())
