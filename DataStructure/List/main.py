import pandas as pd
import numpy as np

import sys
sys.path.append("C:\workplace\git\PythonAlgorithm\DataStructure\List")
from linked_list import Node, doubleNode
from stack import Lifo

#simple linked list
node1 = Node('a')
node2 = Node('b') 
node3 = Node('c') 
node1.link = node2
node2.link = node3

def find_data(head, find):
    #포인트
    point = head
    while point.data != find:
        point = point.link
        if point == None:
            print("리스트에 값이 없습니다.")
            break
    return point
def check_bracket(li):
    st = Lifo(len(li))
    for i in li:
        if i == ('('or'['or'{'or'<'):
            st.push(i)