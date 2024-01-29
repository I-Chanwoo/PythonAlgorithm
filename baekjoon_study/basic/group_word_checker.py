def is_group_word(input):
    li_input = list(input)
    if len(li_input) == len(set(li_input)):
        return True
    else:
        for i in list(set(li_input)):
            if input.count(i) != 1:
                if input.replace(i, '') == input.replace(i*input.count(i), ''):
                    pass
                else:
                    return False
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