data = open("data.txt", "r")
dataArray = data.read().splitlines()

validpwds = 0

for x in dataArray:
    x = x.replace(":","",1)
    x = x.replace("-"," ",1)
    x = x.rsplit(' ',3)
    
    low = int(x[0])
    high = int(x[1])
    char = x[2]
    pwd = x[3]

    count = 0
    for i in pwd:
        if i == char:
            count += 1
    if low <= count <= high:
        validpwds += 1

print(validpwds)
