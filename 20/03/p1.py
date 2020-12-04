data = open("data.txt","r")
dataArray = data.read().splitlines()

height = len(dataArray)
width = len(dataArray[0])
down = 1
right = 1
treecount = 0
iteration = 0

xindex = 0
yindex = 0

for x in range(int(round(height/down))):
    iteration += 1
    xindex += right 
    yindex = down*(iteration)

    print(xindex,'x')
    #print(yindex,'y')
    if xindex >= width:
        xindex -= 30
        print('aaaaaa')

    #print(dataArray[yindex][xindex],'here')
    if(dataArray[yindex][xindex])=='#':
        treecount +=1
    #print(iteration,'it')
    print(width,'width')
    #print(treecount,'trees')
#    print(type(xindex))
#    print(type(width))
    input('')
