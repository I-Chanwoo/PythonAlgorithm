#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import random
import copy


# In[3]:


array_8 = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 0],  9)
puzzle = [[np.nan,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,np.nan,np.nan]]
answer = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]#goal_state


# In[4]:


num = 0
for i in range(0,3):
    for j in range(0,3):
        puzzle[i][j] = array_8[num]
        num += 1


# In[14]:


correct_num =list(np.equal(answer[0],puzzle[0])).count(True)+list(np.equal(answer[1],puzzle[1])).count(True)+list(np.equal(answer[2],puzzle[2])).count(True)


# In[5]:


def count_correct(vector1, vecter2, vector1_case, vecter2_case, add, exadd):
    assume = copy.deepcopy(add)
    assume[vector1][vecter2] = assume[vector1_case][vecter2_case]
    assume[vector1_case][vecter2_case] = 0
    correct_num =list(np.equal(answer[0],assume[0])).count(True)+list(np.equal(answer[1],assume[1])).count(True)+list(np.equal(answer[2],assume[2])).count(True)
    if assume == exadd:
        correct_num = -1
    return correct_num, assume


# In[36]:


def compare(case1, case2, case3=[0], case4 =[0]):
    dic = {case1[0]:case1, case2[0]:case2, case3[0]:case3, case4[0]:case4}
    li = [case1[0], case2[0], case3[0], case4[0]]
    maximum = max(li)

    return dic[maximum][1]


# In[74]:


#8-puzzle function

def solve8puzzle(quiz, exquiz):
    first = '' #vector 1
    second = '' #vector 2

    for i in range(len(quiz)):
            for j in range(len(quiz[i])):
                    if quiz[i][j] == 0:
                            first = i #first vector where zero is
                            second = j #second vector where zero is
    if first == 0:
        if second == 0:
            case1 = count_correct(0, 0, 0, 1, quiz, exquiz)
            case2 = count_correct(0, 0, 1, 0, quiz, exquiz)
            quiz = compare(case1, case2)
        elif second == 1:
            case1 = count_correct(0, 1, 0, 2, quiz, exquiz)
            case2 = count_correct(0, 1, 0, 0, quiz, exquiz)
            case3 = count_correct(0, 1, 1, 1, quiz, exquiz)
            quiz = compare(case1, case2, case3)
        else:
            case1 = count_correct(0, 2, 0, 1, quiz, exquiz)
            case2 = count_correct(0, 2, 1, 2, quiz, exquiz)
            quiz = compare(case1, case2)

    elif first == 1:
        if second == 0:
            case1 = count_correct(1, 0, 1, 1, quiz, exquiz)
            case2 = count_correct(1, 0, 2, 0, quiz, exquiz)
            case3 = count_correct(1, 0, 0, 0, quiz, exquiz)
            quiz = compare(case1, case2, case3)
        elif second == 1:
            case1 = count_correct(1, 1, 1, 2, quiz, exquiz)
            case2 = count_correct(1, 1, 1, 0, quiz, exquiz)
            case3 = count_correct(1, 1, 2, 1, quiz, exquiz)
            case4 = count_correct(1, 1, 0, 1, quiz,exquiz)
            quiz = compare(case1, case2, case3, case4)
        else:
            case1 = count_correct(1, 2, 1, 1, quiz, exquiz)
            case2 = count_correct(1, 2, 2, 2, quiz, exquiz)
            case3 = count_correct(1, 2, 0, 2, quiz, exquiz)
            quiz = compare(case1, case2, case3)   
    else:
        if second == 0:
            case1 = count_correct(2, 0, 2, 1, quiz, exquiz)
            case2 = count_correct(2, 0, 1, 0, quiz, exquiz)
            quiz = compare(case1, case2)

        elif second == 1:
            case1 = count_correct(2, 1, 2, 2, quiz, exquiz)
            case2 = count_correct(2, 1, 2, 0, quiz, exquiz)
            case3 = count_correct(2, 1, 1, 1, quiz, exquiz)
            quiz = compare(case1, case2, case3)
        else:
            case1 = count_correct(2, 2, 2, 1, quiz, exquiz)
            case2 = count_correct(2, 2, 1, 2, quiz, exquiz)
            quiz = compare(case1, case2)

    return quiz


# In[73]:





# In[70]:





# In[71]:





# In[66]:





# In[59]:


count_correct(2, 2, 1, 2, [[5, 4, 8], [1, 0, 6], [7, 2, 3]], [[5, 0, 8], [1, 4, 6], [7, 2, 3]])


# In[87]:


result = solve8puzzle(puzzle, [])
ex_array = puzzle.copy() 
i = 0

while (list(np.equal(answer[0],result[0])).count(True)+list(np.equal(answer[1],result[1])).count(True)+list(np.equal(answer[2],result[2])).count(True)) < 6:
    save = result.copy()
    result = solve8puzzle(result, ex_array)
    ex_array = save
    i += 1
    print(i)
    print(result)


# In[78]:


list(np.equal(answer[0],puzzle[0])).count(True)+list(np.equal(answer[1],puzzle[1])).count(True)+list(np.equal(answer[2],puzzle[2])).count(True)


# In[85]:


result = [[0, 7, 6], [3, 5, 8], [1, 4, 2]]
list(np.equal(answer[0],result[0])).count(True)+list(np.equal(answer[1],result[1])).count(True)+list(np.equal(answer[2],result[2])).count(True)


# In[ ]:




