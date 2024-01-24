from datatime import *
from random import *
#Praktiline töö
#Ülesanne 1
nimi=input("Palun sisesta oma nimi´:")
mitu=int(input("Mitukorda tervitada? "))
for i in range(mitu):
    print(f"Ole tervitud, {nimi}, {i+1}. korda.")

#Ülesanne 2
sum_=0
for i in range(10):
    arv=int(input("Sisesta arv:"))
    sum_+=arv
print(f"Summa= {sum_}")

Ülesanne 2.1
sum_=0
i=0
while True:
    i+=1
    arv=int(input("Sisesta arv: "))
    if i>10: break
    if arv==777: break
    sum_+=arv
print(f"Summa= {sum_}")

#Ülesanne 3
K=0
while True:
    K+=1
    print(f"{k}. ülesanne")
    a=randint(1,50)
    b=randint(1,50)
    p=5
    while True:
        v=int(input(f"{a}+{b}= "))
        p-=1
        if v==a+b:
            print("Õige vastus!")
            break
        elif p==0:
                
        print(f"{a}+{b}={a+b}")
        break
    if k==10: break

#Ülesanne 4

for i in range(1,11):
    for j in range(1.11):
        print(f"{i}*{j}={i*j}")

#Ülesanne 5

for i in range(1,11):
    for j in range(1,11):
        print(f"0",end="")
        print()
