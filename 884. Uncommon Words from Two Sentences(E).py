A = "this apple is sweet"
B = "this apple is sour"

S = A.split() + B.split()
h = dict()
for i in S: h[i] = h.get(i,0) + 1
print([s for s,c in h.items() if c == 1])