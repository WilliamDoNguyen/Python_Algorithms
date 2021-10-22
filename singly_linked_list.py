class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def addToFront(self, valueInput):
        if self.head != None:
            newNode = Node(valueInput)
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
            return self

    def addToBack(self, valueInput):
        newNode = Node(valueInput)
        if self.head == None:
            self.head = newNode
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = newNode
        return self

    def display(self):
        runner = self.head
        result = ""
        while runner != None:
            result += f"{runner.value}-->"
            runner = runner.next
        print(result)
        return self

    def contain(self, valueToFind):
        if self.head == None:
            print("You think this is a joke??! No node, man.")
            return False
        else:
            runner = self.head
            while runner!= None:
                if runner.value == valueToFind:
                    print("I gotchu, fam! We found it!")
                    return True
                runner = runner.next

            print("The number you have dialed is unavailable.")
            return False

    def removeFront(self):
        if self.head != None:
            self.head = self.head.next
        else:
            return False
        return self

    def removeTail(self):
        if self.head == None:
            print("Bwam-bwam. Try again.")
            return self
        elif self.head.next == None:
            self.head = None
            return self
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        runner.next = None
        return self

    def minToFront(self):
        if self.head == None:
            return False
        minnode = self.head
        runner = self.head
        prev = self.head
        while runner.next != None:
            if minnode.value > runner.next.value:
                prev = runner
                minnode = runner.next
            runner = runner.next
        prev.next = minnode.next
        minnode.next = self.head
        self.head = minnode

    def maxToBack(self):
        if self.head == None:
            return False
        maxnode = self.head
        runner = self.head
        prev = self.head
        while runner.next != None:
            if maxnode.value < runner.next.value:
                prev = runner
                maxnode = runner.next
            runner = runner.next
        prev.next = maxnode.next
        runner.next = maxnode
        maxnode.next = None

    # def prepend(self, node1, node2):
    #     if self.checker(node1) == True:
    #         runner = self.head
    #         while runner.next.value != node1:
    #             runner = runner.next
    #         node2.next = runner.next
    #         runner.next = node2
    #         return self
    #     else:
    #         return False
    # def append(self, node1, node2):
    #     if self.checker(node1) == True:
    #         runner = self.head
    #         while runner.value != node1:
    #             runner = runner.next
    #         node2.next = runner.next
    #         runner.next = node2
    #         return self
    #     else:
    #         return False

    def prepend(self,a,b):
        is_there= self.contain(a)
        result = ""
        if is_there == True:
            runner = self.head
            while runner.value != a:
                result += f"{runner.value}-->"
                runner = runner.next
            result += f"{b}-->"
            result += f"{runner.value}-->"
            while runner.next != None:
                runner = runner.next
                result += f"{runner.value}-->"
            print(result)
            return self
        else:
            print("Value not found in singly-linked list")
            return False

    def append(self, a, b):
        is_there= self.contain(a)
        result = ""
        if is_there == True:
            runner = self.head
            while runner.value != a:
                result += f"{runner.value}-->"
                runner = runner.next
            result += f"{runner.value}-->"
            result += f"{b}-->"
            while runner.next != None:
                runner = runner.next
                result += f"{runner.value}-->"
            print(result)
            return self
        else:
            print("Value not found in singly-linked list")
            return False

    def removeNegative(self):
        runner = self.head
        while runner.next != None:
            if runner.next.value < 0:
                runner.next = runner.next.next
            else:
                runner = runner.next
        if self.head.value < 0:
            self.head = self.head.next
        return self

sl_list = SLL()
sl_list2 = SLL()
sl_list3 = SLL()

sl_list.addToBack(-1).addToBack(7).addToBack(13).addToBack(9001).addToFront(26).removeNegative().display()
sl_list2.addToBack(-2).addToBack(3).addToBack(-4).addToFront(-1).removeNegative().display()
sl_list3.addToBack(-2).addToFront(-1).removeNegative().display()
# sl_list.contain(7)
# sl_list.contain(-50)
# sl_list.removeFront().removeFront().removeTail().display()

# sl_list2.removeTail()
