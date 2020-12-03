data = open("data.txt", "r")
dataArray = data.read().splitlines()
for x in dataArray:
    for y in dataArray:
        for z in dataArray:
            if int(x)+int(y)+int(z) == 2020:
                print('{} + {} + {} = 2020. The product is {}.'.format(x,y,z,int(x)*int(y)*int(z)))
                exit()
