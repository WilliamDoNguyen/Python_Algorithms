# ARRAY STACK
class ArrStack:
    def __init__(self):
        self.list = []

    # Add to top of stack
    def add(self, value):
        self.list.append(value)

    # Remove from top of stack
    def remove(self):
        self.list.pop()

    # Return value at top of stack
    def get_top(self):
        print(self.list[-1])
        return self.list[-1]

    # Return size of stack
    def size(self):
        print(len(self.list))
        return len(self.list)

    # Return if a particular value is contained in the stack
    def contain(self,value):
        for i in self.list:
            if i == value:
                print("Found it!")
                return True
        print("Didn't find it...")
        return False

    # Return if stack is empty
    def is_empty(self):
        if len(self.list) == 0:
            print("The list is empty!")
            return True
        else:
            print("The list is NOT empty!")
            return False

    def print_list(self):
        print(self.list)

# arr = ArrStack()
# arr.is_empty()
# arr.add(1)
# arr.is_empty()
# arr.add(2)
# # arr.remove()
# arr.add(3)
# arr.get_top()
# arr.remove()
# arr.get_top()
# arr.print_list()
# arr.size()
# arr.contain(1)
# arr.contain(4)
# Node class
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
# SLL STACK
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
slist = SLLStack()

slist.is_empty()
slist.add(1)
slist.is_empty()
slist.add(2)
slist.add(3)
slist.return_top()
slist.remove()
slist.return_top()
slist.display()
slist.size()
slist.contains(1)
slist.contains(4)
