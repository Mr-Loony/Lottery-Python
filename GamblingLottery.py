from random import randint, random
num2 = []
numm3 = []
maxnr = 0
minnr = 100
print("Welcome to Solomon's Lottery!")
n = int(input("Enter sum: "))
for k in range(5):
    m = int(input("Please enter number: "))
    num2.append(m)
x = 0
num=[]
for i in range(10):
    random=randint(1,20)
    while random in num:
        random=randint(1,20)
    num.append(random)


for nr in num2:
    if nr in num:
        x = x+1

print(num2)
print(num)
print("You won: ", n*x)