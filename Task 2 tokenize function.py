#TASK
"""
Task 2 :-
Write a function tokenize(s) that takes a string "s"
and returns a list of tokens:

Example:-
Input :- "NLP is EASY"
Output :- ["NLP","is","EASY"]
"""

#CODE
def tokenize(s = str()):
    List = s.split(" ")
    List = [""]+List
    Keys = [i for i in range(len(List))]
    List = dict(zip( Keys, List ))
    return List
data = tokenize("NLP is easy")
print(data)

