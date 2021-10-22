class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLLStack:
    def __init__(self):
        self.top = None

    # Add to top of stack
    def add(self, value):
        if self.top == None:
            self.top = Node(value)
        else:
            newnode = Node(value)
            newnode.next = self.top
            self.top = newnode

    # Remove from top of stack
    def remove(self):
        if self.top == None:
            print("Nothing to remove!")
            return False
        else:
            self.top = self.top.next

    # Return value at top of stack
    def return_top(self):
        print(self.top.value)
        return self.top.value
# Return size of stack
    def size(self):
        if self.top == None:
            print("No list to count!")
            return 0
        else:
            count = 0
            runner = self.top
            while runner != None:
                count += 1
                runner = runner.next
            print(count)
            return count

    # Return if a particular value is contained in the stack
    def contains(self, value):
        if self.top == None:
            print("No list, no value!")
            return False
        else:
            runner = self.top
            while runner != None:
                if runner.value == value:
                    print("Found it!")
                    return True
                runner = runner.next
            print("Never found it")
            return False

    # Return if stack is empty
    def is_empty(self):
        if self.top == None:
            print("The list is empty!")
            return True
        else:
            print("The list is NOT empty")
            return False

    def display(self):
        if self.top == None:
            print("No list to display")
        else:
            result = ""
            runner = self.top
            while runner.next != None:
                result += f"{runner.value} -> "
                runner = runner.next
            result += f"{runner.value}"
            print(result)

    def pop(self):
        temp = self.top.value
        self.top = self.top.next
        return temp

class TSQ:
    def __init__(self):
        self.stack1 = SLLStack()
        self.stack2 = SLLStack()

    def enqueue(self,value):
        self.stack1.add(value)
        return self

    def dequeue(self):
        while self.stack1.size() > 0:
            to_add = self.stack1.pop()
            self.stack2.add(to_add)

    def display2(self):
        if self.stack2.top == None:
            print("No list to display")
        else:
            result = ""
            runner = self.stack2.top
            while runner.next != None:
                result += f"{runner.value} -> "
                runner = runner.next
            result += f"{runner.value}"
            print(result)

list_one = TSQ()
list_one.enqueue(5).enqueue(27).enqueue(13).dequeue()
list_one.display2()
