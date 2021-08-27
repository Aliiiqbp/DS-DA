#!/usr/bin/env python3

class Node:
    def __init__(self, label, number, parent):
        self.right_child = None
        self.left_child = None
        self.parent = parent
        self.number = number
        self.label = label

def insert(root, label):
    if label == root.label:
        root.number += 1
    elif label < root.label:
        if root.left_child != None:
            insert(root.left_child, label)
        else:
            root.left_child = Node(label, 1, root)
    else:
        if root.right_child != None:
            insert(root.right_child, label)
        else:
            root.right_child = Node(label, 1, root)

def find_max_node(root, label, node):
    if label != root.label[0:len(label)]:
        #print("hi")
        #print(label)
        #print(root.label[0:len(label)])
        if label < root.label:
            if root.left_child != None:
                return find_max_node(root.left_child, label, node)
            else:
                return node
        else:
            if root.right_child != None:
                #print("hi3")
                return find_max_node(root.right_child, label, node)
            else:
                return node
    else:
        #print("hi2")
        if root.number > node.number:        
            node = root
            if root.left_child != None:
                node = find_max_node(root.left_child, label, node)
            if root.right_child != None:
                node = find_max_node(root.right_child, label, node)
            return node
        else:
            #print("hi4")
            if root.number == node.number and root.label < node.label:
                #print("hi5")
                node = root
            if root.left_child != None:
                node = find_max_node(root.left_child, label, node)
            if root.right_child != None:
                node = find_max_node(root.right_child, label, node)
            return node
            
n = int(input())
root = Node(input(), 1, None)
for i in range(0, n-1):
    insert(root, input())

#print(root.right_child.right_child.label)
    
m = int(input())    
for i in range(0, m):
    node = Node('nothing', -1, None)
    node = find_max_node(root, input(), node)
    if node.number != -1:
        print(node.label)
    print(node.number)
