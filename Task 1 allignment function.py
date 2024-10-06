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
def all_alignments(l = int(),m=int()):
    List = list()
    for i in range(l+1):
        for j in range(m+1):
            a = [i,j]
            List.append(a)
    return List

data = all_alignments(2,2)
print(data)
