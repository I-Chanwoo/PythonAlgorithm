'''
유클리드 호제법
 1.두 수 중 더 작은 수로 나눔
 2. 나머지가 0이 아니라면 작은수를 나머지로 나눔 
 3. 나머지가 0이 될 때까지 1, 2 반복
 4, 나머지가 0이 되었을 때의 몫이 최대공
'''

def common_divisior(input1, input2):
    max_input = max(input1,input2)
    min_input = min(input1, input2)
    
    remain = max_input%min_input
    if (remain == 0):
        greatest  = min_input
        return int(greatest)
    else:
        greatest  = max_input/min_input

    while(True):
        if (remain == 0):
            return int(greatest)
        max_input = max(min_input, remain)
        min_input = min(remain, min_input)
        greatest  = max_input/(max_input/min_input)
        remain = max_input%min_input

x1 = int(input("정수를 입력하세요:"))
x2 = int(input("정수를 입력하세요:"))
print(common_divisior(x1,x2)) 

