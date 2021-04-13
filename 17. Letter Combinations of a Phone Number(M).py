digits = "23"

l = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
d = list(map(int,digits))
r = []
while d:
    c = d.pop(0)
    if r == []: r = l[c]
    else: r = [a+b for a in r for b in l[c]]

print(r)