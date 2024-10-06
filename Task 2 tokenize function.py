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
    return s.split(" ")
data = tokenize("NLP is easy")
print(data)

#ANOTHER OPTION
def tokenize(s = str()):
    l = list()
    pointer = 0
    for i in range(len(s)):
        if s[i] == " " :
            l.append(s[pointer:i])
            pointer = i+1
    l.append(s[pointer:])
    return l
data = tokenize("NLP is easy")
print(data)

