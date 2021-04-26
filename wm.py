#This program uses the Weighted Majority Algorithm
from decimal import Decimal
from math import log
#Get Stream
f = open("sample.txt","r")
raw = f.readlines()
data = {}
for i in range(len(raw)):
    temp = raw[i].split()
    data[i] = temp

#initialize all variables
eta_val = float(0.01)
w_vec = [float(1.00) for x in range(16)]

#expert_vec = [0 for x in range(16)]
mistake_expert = [0 for x in range(16)]
mistake_ctr = 0

for t in data:
    e_vec = data[t][0]
    alpha_val = 0.00
    beta_val = 0.00
    for j in range(16):
        if e_vec[j] == '1':
            alpha_val += w_vec[j]
        if e_vec[j] == '0':
            beta_val += w_vec[j]

    policy = '0'
    if alpha_val >= beta_val:
        policy = '1'
    
    real_val = data[t][1]

    if policy != real_val:
        mistake_ctr += 1

    for i in range(16):
        if e_vec[i] != real_val:
            w_vec[i] = w_vec[i] *(1 - eta_val)
            mistake_expert[i] += 1

#find best expert
best_val = max(w_vec)
expert = 0
for i in range(16):
    if w_vec[i] == best_val:
        expert = i
        break

print("Number of Mistakes by Algorithm: " + str(mistake_ctr))
print("Number of Mistakes by Best Expert " + str(expert), end ="")
print(": " + str(mistake_expert[expert]))

regret_bound = 2*(1+(eta_val))*mistake_expert[expert] + (2*log(16))/(eta_val)

print("Regret Bound <= " + str(regret_bound))
