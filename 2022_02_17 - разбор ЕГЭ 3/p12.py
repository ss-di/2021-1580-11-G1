def work(s):
    while '00' not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)
    return s

def stat(s):
    return s.count('1'), s.count('2'), s.count('3'),

itog = []

for i1 in range(1, 50):
    for i2 in range(1, 50):
        for i3 in range(1, 50):
            print(i1, i2, i3)
            s = '0'+'1'*i1+'2'*i2+'3'*i3+'0'
            res = work(s)
            st = stat(res)
            if st == (70, 56, 23):
                itog.append((len(s), s))
                
print(itog)
