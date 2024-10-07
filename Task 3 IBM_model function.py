#TASK
"""
Task 3 :-
Build a IBM_model(f,e,m) that it takes , two strings f , e and integer
m and returns the value of P(f|e,m)

for now ,
1. Assume m = l
2. Write a function "word_prob(wf,we_a)" where wf and we_a are
   the words and always returns the value 0.5
"""
#CODE

def tokenize(s = str()):
    List = s.split(" ")
    List = [""]+List
    Keys = [i for i in range(len(List))]
    List = dict(zip( Keys, List ))
    return List

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

def word_prob(wf = str(),we_a = str()):
    return 0.5

def IBM_model(f,e,m):
    l = m
    probability_sum = 0
    Total_alignments = all_alignment(l,m)
    f_tokens = tokenize(f)
    e_tokens = tokenize(e)
    x = 1/((1+l)**m)
    for i in Total_alignments:
        product = 1
        for j in range(1,m+1):
            wf = f_tokens[j]
            we_a = e_tokens[i[j]]
            product = product * word_prob(wf, we_a)
        iteration_result = x * product
        probability_sum += iteration_result
    return probability_sum

f = "Mein name ist Steven"
e = "My name is Steven"
m = len(tokenize(f))-1
data = IBM_model(f,e,m)
print(data)

            
            
        
