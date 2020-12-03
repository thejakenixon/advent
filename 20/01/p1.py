data = open("data.txt", "r")
dataArray = data.read().splitlines()
for x in dataArray:
    for y in dataArray:
        if int(x)+int(y) == 2020:
            print('{} + {} = 2020. The sum is {}.'.format(x,y,int(x)*int(y)))
            exit()
