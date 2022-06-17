'''
1 2 3 4 5 6 7 8 9 10 11 12
9 9 9 9 9 9 9 9 9  9  9 0-9 11*(10-3)+ (10-1-3)
9 9 9 9 9 9 9 9 9  9  6  3  12*11
9 9 9 9 9 9 9 9 9  6  6  6  12*11*10/6  
'''

def f(num):
    if len(num) == 12 and sum(filter(lambda x: x%3==0, num))==99:
        return 1
    if len(num) == 12 or 9*(12-len(num)) < 99-sum(filter(lambda x: x%3==0, num)):
        return 0
    res = 0
    for d in range(0 if len(num)>0 else 1, 10):
        res += f(num + [d])
    return res

print(f([]))
