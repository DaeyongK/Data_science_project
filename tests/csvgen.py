import random
string = ''
for i in range(0, 100000):
    string = string + str(random.randint(0, 50000))+ ','

print(string)
