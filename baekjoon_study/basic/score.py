def calculate_grade(input):
    sum_ = 0
    credit = 0
    for i in input:
        if i[1] == "A+":
            sum_ += 4.5*i[0]
            credit += i[0]
        elif i[1] == "A0": 
            sum_ += 4.0*i[0]
            credit += i[0]
        elif i[1] == "B+": 
            sum_ += 3.5*i[0]
            credit += i[0]
        elif i[1] == "B0": 
            sum_ += 3.0*i[0]
            credit += i[0]
        elif i[1] == "C+": 
            sum_ += 2.5*i[0]
            credit += i[0]
        elif i[1] == "C0": 
            sum_ += 2.0*i[0]
            credit += i[0]
        elif i[1] == "D+": 
            sum_ += 1.5*i[0]
            credit += i[0]
        elif i[1] == "D0":
            sum_ += 1.0*i[0]
            credit += i[0]
        elif i[1] == "F":
            credit += i[0]
        else: 
            pass
    if credit == 0:
        return float(0)
    return sum_/credit

li_grade = [[3.0,"A+"],
 [3.0,"A+"],
 [3.0,"A0"],
 [3.0,"A+"],
 [3.0,"A+"],
 [3.0,"B0"],
 [3.0,"A0"],
 [3.0,"B0"],
 [3.0,"B0"],
 [3.0,"C+"],
 [3.0,"B0"],
 [4.0,"A+"],
 [3.0,"B+"],
 [3.0,"C0"],
 [3.0,"D+"],
 [3.0,"C+"],
 [3.0,"B0"],
 [3.0,"B+"],
 [3.0,"D0"],
 [4.0,"P"]]

li_grade2 = [[3.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"P"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"P"],
 [3.0,"P"],
 [3.0,"P"],
 [4.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [3.0,"F"],
 [4.0,"P"]]

print(calculate_grade(li_grade))
print(calculate_grade(li_grade2))