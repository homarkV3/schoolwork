from tkinter.messagebox import NO
from turtle import done


class CourseList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, COURSE):
        ptNode = self.head
        done = False

        if self.head == None:
            self.head = COURSE
            self.tail = COURSE
            return COURSE

        while done == False:
            if ptNode.next == None:
                self.tail = COURSE
                done = True
            elif ptNode.next.number <= COURSE.number:
                tempNode = ptNode.next
                COURSE.next = tempNode
                ptNode.next = COURSE
                done == True
            else:
                ptNode = ptNode.next

    def remove(self, NUMBER):
        ptNode = self.head
        done = False

        while done == False:
            if ptNode == None:
                done = True
            elif ptNode.next.number == NUMBER:
                ptNode.next = ptNode.next.next
                done = True
            else:
                ptNode = ptNode.next
                

    def remove_all(self, NUMBER):
        ptNode = self.head
        done = False

        while done == False:
            if ptNode == None:
                done = True
            elif ptNode.next.number == NUMBER:
                ptNode.next = ptNode.next.next
                done = True
            else:
                ptNode = ptNode.next

    def find(self, NUMBER):
        ptNode = self.head
        done = False

        while done == False:
            if ptNode == None:
                return -1
            elif ptNode.number == NUMBER:
                return ptNode
            else:
                ptNode = ptNode.next
    
    def size(self):
        count = 0
        ptNode = self.head
        done = False

        while done == False:
            if ptNode == None:
                done = True
            else:
                count += 1
                ptNode = ptNode.next
        return count
    
    def calculate_gpa(self):
        total = 0.0
        ptNode = self.head
        done = False

        while done == False:
            if ptNode == None:
                done = True
            else:
                total += ptNode.grade
                ptNode = ptNode.next
        return total

    def is_sorted(self):
        ptNode = self.head
        done = False

        while done == False:
            if ptNode == None:
                done = True
            elif ptNode.number > ptNode.next.number:
                return False
            else:
                ptNode = ptNode.next
        return True

    def __str__(self):
        ptNode = self.head
        linkedStr = ""

        for i in range(self.size):
            linkedStr += f"{ptNode.__str__}\n"
            ptNode = ptNode.next
        return linkedStr