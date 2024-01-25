
def count_croatia(input):
    count = len(input)
    for i in ['c=','c-','d-','lj','nj','s=','z=']:
        if(i == 'z='):
            if(input.count('dz=')!=0):
                count -= 2*input.count('dz=')
                input = input.replace('dz=','')
        count -= 1*input.count(i)
    return count
print(count_croatia(input()))
