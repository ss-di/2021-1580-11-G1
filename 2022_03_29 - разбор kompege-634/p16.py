rF = {}
rG = {}

def F(n):
    global rF;
    if n in rF:
        return rF[n]
    if n <= 2:
        ans = 1
    elif n % 2 != 0:
        ans = F(n - 1) - n
    else:
        ans = F(n - 2) + G(n - 1) + 2
    rF[n] = ans
    return ans

def G(n):
    global rG;
    if n in rG:
        return rG[n]
    if n <= 0:
        ans = 2
    elif n % 2 != 0:
        ans = F(n - 1) - 2 * G(n - 2)
    else:
        ans = 2 * F(n - 2) - 2 * G(n - 1)
    rG[n] = ans
    return ans
    
print(F(96))
