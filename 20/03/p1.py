data = open("data.txt","r")
dataList = data.read().splitlines()

height = len(dataList)
width = len(dataList[0])
down = 1
right = 3
treecount = 0

x = 0
y = 0

def treeCount(down,right)
while (y <= height-down-1):
    x += right
    y += down

    if x >= (width-right):
        x -= width

    if(dataList[y][x])=='#':
        treecount +=1

print(treecount,'trees')
