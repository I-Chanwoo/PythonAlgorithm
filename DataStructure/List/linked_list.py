import pandas as pd
import numpy as np

#simple linked list
class Node():
    def __init__(self, data):
        self.data = data
        self.link = None

    def current_link(self):
        return self.link
    
    def insert_node(self, newNode):
        newNode.link = self.link
        self.link = newNode
    
    def __del__(self):
        print(self.data + "객체를 삭제합니다")


#double linked list
class doubleNode():
    def __init__(self, data):
        self.data = data
        self.llink = None
        self.llink = None

    def current_llink(self):
        if self.llink == None:
            print("ERROR:: Head Node")
            return
        return self.llink
    
    def current_rlink(self):
        return self.rlink    
    
    def __del__(self):
        print(self.data + "객체를 삭제합니다")