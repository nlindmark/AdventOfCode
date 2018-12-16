import re
from collections import defaultdict

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
       
 
    def __str__(self):
        return (str(self.data))
 
class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None
        self.cur_marble = None
        self.value = 0
 
    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

    def get_after(self, ref_node):
        return ref_node.next

    def get_before(self, ref_node):
        return ref_node.prev


    def insert_first_marble(self):
        new_node = Node(0)
        self.insert_at_end(new_node)
        return(0)

    def insert_marble(self):
        self.value += 1

        if(self.value % 23 != 0):
            new_node = Node(self.value)
            tmp = self.get_after(self.cur_marble)
            self.insert_after(tmp, new_node)
            self.cur_marble = new_node
            return(0)
        else:
            score = self.value
            for i in range(7):
                tmp =self.get_before(self.cur_marble)
                self.cur_marble = tmp
            score += self.cur_marble.data 

            tmp = self.cur_marble.next
            self.remove(self.cur_marble)
            self.cur_marble = tmp

            return(score)



    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)
 
    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.cur_marble = self.first
        else:
            self.insert_after(self.first.prev, new_node)
 
    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.first = new_node
 
    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next
 
    def display(self):
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data)
            current = current.next
            if current == self.first:
                break



def solve(filename):

    
    
    file = open(filename, "r")
    input = file.readlines()
    input = input[0].split(" ")

    file.close()
        
    no_players = int(input[0])
    high_marble = int(input[6])

    d = CircularDoublyLinkedList()
    p = defaultdict(int)

    no = 0
    p[no] = d.insert_first_marble()
    for i in range(1, high_marble):
        no += 1
        if(no % no_players == 0):
            no = 0
        p[no] += d.insert_marble()

    
    return(max(p.values()))

print("Solution is {}".format(solve("puzzledata.txt")))
