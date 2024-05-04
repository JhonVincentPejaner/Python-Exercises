import random

ch = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
num = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'


passw = int(input("Length of a password: "))


chl = int(input("Length of ch: "))
numl = int(input("Length of num: "))

newc = ''
newn = ''
password = ''
for i in range(chl):
    newc += random.choice(ch)

for j in range(numl):
    newn += random.choice(num)

for x in range(passw):
    password = newc + newn + random.choice(ch) + random.choice(num)
    
print(password)

    
       