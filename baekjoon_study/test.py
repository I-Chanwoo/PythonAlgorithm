import numpy as np

#고급인덱싱
arr = [[ j for j in range(1+((i-1)*10),10*(i))] for i in range(1,6)]
arr = np.array(arr)
print(arr[[0, 1, 2], [0, 1, 0]])

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 0]])

##유니버셜리 함수(넘파이에서 제공하는 범용함수, 단일 배열에 사용)