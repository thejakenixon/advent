# Data has been modified:
# F, L are 0
# B, R are 1

data = open('data.txt','r').read().splitlines()

p1=0
p2=127

length = len(data)

def b(p1,p2):
    p1 += math.floor((p2-p1)/2)+1
    return p1

def f(p1,p2):
    p2 -= math.floor((p2-p1)/2)+1

print(data[0][0])
#for x in range(length):
#    print(data[x])
