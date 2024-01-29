def is_group_word(input): #입력받은 단어가 그룹단어인지

    #알파벳이 한 글자도 겹치지 않는 단어인 경우
    li_input = list(input) #단어를 리스트화 ex) list("list") = ['l','i','s','t']
    if len(li_input) == len(set(li_input)): #만일 list(input)과 set(input)의 길이가 같다면 /set은 중복값이 알아서 제거됨
        return True #true return
    
    #겹치는 알파벳이 있는 경우
    else:
        for i in list(set(li_input)):#set(input)에 있는 알파벳을 가져옴
            if input.count(i) != 1:#만일 input.count(i)이 0이 아니라면 = 단어 안에서 알파벳이 한번만 쓰이지 않았다면
                if input.replace(i, '') == input.replace(i*input.count(i), ''):#알파벳을 지운 경우와 알파벳이 전부 붙어 있는 경우를 지운 경우의 값이 같다면
                    pass #건너뜀
                else: #아니라면
                    return False #
        return True
    
def checker(num):
    count = 0
    for i in range(num):
        str = input()
        if is_group_word(str):
            count += 1
    return count

num = int(input())
print(checker(num))