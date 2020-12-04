data = open("data.txt","r")
dataList = data.read().splitlines()

height = len(dataList)
width = len(dataList[0])

def treeCounter(down,right):
    for i in range(0,height):
        x = 0
        y = 0
        treeCount = 0

        while(y <= (height - down - 1)):
            x += right 
            y += down

            if x >= (width-right):
                x -= width

            if((dataList[y][x]=='#')):
                treeCount +=1
    return treeCount

total = treeCounter(1,1)*treeCounter(1,3)*treeCounter(1,5)*treeCounter(1,7)*treeCounter(2,1)
print(total)
