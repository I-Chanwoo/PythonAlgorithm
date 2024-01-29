import pandas as pd
import numpy as np

#lifo는 undo에서 사용되는 data structure

class Lifo():
    #def에 -> None 또는 -> str 로 명시된 경우가 있다. 
    #이는 return 값을 명시해주어 한번에 알아볼 수 있게 하기 위해 적는 것이다
    def __init__(self, len) -> None:
        self.list = []
        self.top = -1
        self.len = len

    def push(self, data) -> None:
        if len(self.list) >= self.len:
            print('ERROR :: full of stack')
            return
        self.top += 1
        self.list.append(data)
        return
     
    def pop(self) -> None:
        if self.top <= -1:
            print("ERROR :: stack is empty")
            return
        data = self.list[self.top]
        del self.list[self.top] #list에서 특정 인덱스의 값 삭제하는 법
        self.top -= 1
        return data