data = open("data.txt","r")
dataArray = data.read().splitlines()

height = len(dataArray)
width = len(dataArray[0])
down = 1
right = 3
treecount = 0

iteration = 0

for x in range(int(round(height/down))):
    iteration += 1
    xindex = right*(iteration)
    yindex = down*(iteration)

    print(xindex)
    print(yindex,'y')
    if xindex >= width: xindex -= width

    #print(dataArray[yindex][xindex])
    if(dataArray[yindex][xindex])=='#':
        treecount +=1
    print(iteration)
    print(treecount)
