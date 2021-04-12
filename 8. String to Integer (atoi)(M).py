# s = "21474836460"
# s = "  0000000000012345678"
# s = "00000-42a1234"
# s = "42"
# s = "  +  413"
s = "   -42"

n, p = '', ''

for i in s:
    
    if i.isdigit() == True: n += i
    
    else:
        if i == ' ' and p + n == '': continue
        elif i in ['+','-'] and p + n == '': p = i
        else: break

n = 0 if n == '' else int(p+n)

if n >= 2**31-1: n = 2**31-1
elif n <= -2**31: n = -2**31

print(n)
