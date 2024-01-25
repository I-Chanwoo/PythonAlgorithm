def continuous(input):
    num = 1
    min = int(input/2)
    max = input-min

    while (min>=1):

        if(max == min+1):
            num += 1

        if(max == 2*min-3):
            num += 1

        ori_min = min

        min = int(max/2)
        max = ori_min

        print(min, max)

    return num

print(continuous(15))
