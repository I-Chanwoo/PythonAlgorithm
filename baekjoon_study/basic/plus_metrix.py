def plus_metrix(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            print(m1[i][j]+m2[i][j], end=" ")
        print()  

a, b = input().split()
li= []
for i in range(2):
    li.append([list(map(int, input().split())) for _ in range(int(a))])

plus_metrix(li[0],li[1])
