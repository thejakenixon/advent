data = open("data.txt","r")
dataList = data.read().splitlines()

height = len(dataList)
width = len(dataList[0])
down = 2
right = 1
treecount = 0
iteration = 0

xindex = 0
yindex = 0

for x in range(height):
    iteration += 1
    xindex += right 
    yindex = down*(iteration)

    if xindex >= width:
        xindex -= width

#    print(dataList[yindex][xindex],'here')
    if(dataList[yindex][xindex])=='#':
        treecount +=1
    print(treecount,'trees')
