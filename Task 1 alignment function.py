#TASK
"""
Task 1:- Concept of allignment function in very important in IBM Model 1.
Your task is to write a function named all_allignment(l,m) that takes two integers
"l" and "m" and returns a list of list of all possible allignments .

l = length of total entity in english
m = estimated total length after translation

e.g.  Input l=2,m=2
Output : [0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]
"""
#CODE
def all_alignment(l,m):
    Range = (1+l)**m
    Keys = [i for i in range(1,m+1)]
    alignment = list()
    d = l+1
    for i in range(Range):
        n = i
        q = int()
        r = int()
        one_alignment = list()
        for j in range(m):
            q = n // d
            r = n % d
            one_alignment.append(r)
            n = q
        one_alignment = one_alignment[::-1]
        one_alignment = dict(zip(Keys , one_alignment))
        alignment.append(one_alignment)
    return alignment
l = 4
m = 4
data = all_alignment(l,m)
print(data)
print(len(data))
