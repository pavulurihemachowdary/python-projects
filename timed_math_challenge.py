import random
import time
operators=["+","-","*",]
Min_operand=3
Max_operand=12
min_operations=5

def generate_problem():
    left=random.randint(Min_operand,Max_operand)
    right=random.randint(Min_operand,Max_operand)
    op=random.choice(operators)
    expr=str(left)+op+str(right)
    res=eval(expr)
    return expr,res
wrong=0
input("Press enter to start !")
print("-----------------")
start_time=time.time()

for i in range(min_operations):
    expr,ans=generate_problem()
    guess=input("Problem "+"str(i+1) "+expr+" = ")
    while True:
        if guess==str(ans):
            break
        wrong+=1
end_time=time.time()
tot_time=round(end_time-start_time,2) 

print("------------------")
print("Nice!!,You completed in",tot_time," seconds")
