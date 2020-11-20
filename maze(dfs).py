######################  This is a program of DFS(depth first search) coded by flame.qi#######################
puzzle=\
    [[1,1,1,0,1,1,1],\
     [1,0,0,0,0,0,1],\
     [1,0,1,1,1,0,1],\
     [1,0,1,0,0,0,1],\
     [1,1,1,0,1,1,1],\
     [1,0,0,0,0,0,1],\
     [1,0,1,1,1,0,1],\
     [1,0,0,0,1,0,1],\
     [1,1,1,0,1,1,1]]

# puzzle=\
#     [[1,1,1,0,1,1,1],\
#      [1,0,0,0,0,0,1],\
#      [1,0,1,1,1,0,1],\
#      [1,0,1,0,0,0,1],\
#      [1,1,1,0,1,1,1],\
#      [1,0,0,0,0,0,1],\
#      [1,0,1,1,1,0,1],\
#      [1,1,0,0,1,0,1],\
#      [1,1,1,0,1,1,1]]

print(puzzle[0][3])
XLEN=6
YLEN=8
startP=[3,0]
endP=[3,8]
pathList=[[[[0,0],0,{'up':0,'down':0,'left':0,'right':0}]]]# index 1:x index 2:y index 3:re
uav=[{'x':startP[0],'y':startP[1],'preX':0,'preY':0,'steps':0,'currDir':'down','dir':{'up':0,'down':0,'left':0,'right':0}}]
#pathList.append([8,3,0])
x=startP[0]
y=startP[1]
preX=0
preY=0
steps=0
currDir="down"
dir={'up':0,'down':0,'left':0,'right':0}
for pu in puzzle:
    print (pu)
print("#############################")


while (pathList[0][len(pathList[0])-1][0]!=endP):
    for index in range(len(uav)):
        uav[index]['dir']={'up':0,'down':0,'left':0,'right':0}
    
        if (uav[index]['x']>=0 and uav[index]['x']<XLEN):
            if(puzzle[uav[index]['y']][uav[index]['x']+1]==0):
                uav[index]['dir']['right']=1
            else:
                uav[index]['dir']['right']=0

        if (uav[index]['y']>=0 and uav[index]['y']<YLEN):
            if(puzzle[uav[index]['y']+1][uav[index]['x']]==0):
                uav[index]['dir']['down']=1
            else:
                uav[index]['dir']['down']=0
        if (uav[index]['x']>=1 and uav[index]['x']<=XLEN):
            if(puzzle[uav[index]['y']][uav[index]['x']-1]==0):
                uav[index]['dir']['left']=1
            else:
                uav[index]['dir']['left']=0

        if (uav[index]['y']>=1 and uav[index]['y']<=YLEN):
            if(puzzle[uav[index]['y']-1][uav[index]['x']]==0):
                uav[index]['dir']['up']=1
            else:
                uav[index]['dir']['up']=0
        #print (dir)
        uav[index]['preX']=uav[index]['x']
        uav[index]['preY']=uav[index]['y']
        tempDir=uav[index]['currDir']
        if(tempDir=='down' ):
            if (uav[index]['dir']['down']):
                uav[index]['y']=uav[index]['y']+1
                uav[index]['currDir']="down"
            else:
                if (uav[index]['dir']['left']):
                    uav[index]['x']=uav[index]['x']-1
                    uav[index]['currDir']="left"
                else:
                    if (uav[index]['dir']['right']):
                        uav[index]['x']=uav[index]['x']+1
                        uav[index]['currDir']="right"
                    else:
                        uav[index]['y']-=1
                        uav[index]['currDir']="up"
        if(tempDir=='up' ):
            if (uav[index]['dir']['up']):
                uav[index]['y']=uav[index]['y']-1
                uav[index]['currDir']="up"
            else:
                if (uav[index]['dir']['right']):
                    uav[index]['x']=uav[index]['x']+1
                    uav[index]['currDir']="right"
                else:
                    if (uav[index]['dir']['left']):
                        uav[index]['x']=uav[index]['x']-1
                        uav[index]['currDir']="left"
                    else:
                        uav[index]['y']+=1
                        uav[index]['currDir']="down"
        if(tempDir=='left' ):
            if (uav[index]['dir']['left']):
                uav[index]['x']=uav[index]['x']-1
                uav[index]['currDir']="left"
            else:
                if (uav[index]['dir']['up']):
                    uav[index]['y']=uav[index]['y']-1
                    uav[index]['currDir']="up"
                else:
                    if (uav[index]['dir']['down']):
                        uav[index]['y']=uav[index]['y']+1
                        uav[index]['currDir']="down"
                    else:
                        uav[index]['x']+=1
                        uav[index]['currDir']="right"               
        if(tempDir=='right' ):
            if (uav[index]['dir']['right']):
                uav[index]['x']=uav[index]['x']+1
                uav[index]['currDir']="right"
            else:
                if (uav[index]['dir']['down']):
                    uav[index]['y']=uav[index]['y']+1
                    uav[index]['currDir']="down"
                else:
                    if (uav[index]['dir']['up']):
                        uav[index]['y']=uav[index]['y']-1 
                        uav[index]['currDir']="up"
                    else:
                        uav[index]['x']-=1
                        uav[index]['currDir']="left"

        if (pathList[0][len(pathList[0])-2][0]==[uav[index]['preX'],uav[index]['preY']]):
            pathList[0].pop()
            uav[index]['steps']-=1
        else:
            
            pathList[0].append([[uav[index]['preX'],uav[index]['preY']],uav[index]['steps'],uav[index]['dir']])
            uav[index]['steps']+=1
            
        print ("X="+str(uav[index]['x'])+"Y="+str(uav[index]['y'])+"steps="+str(uav[index]['steps'])+"currDir="+uav[index]['currDir'])
    
print('Output the result of DFS:')
for j in range(len(pathList)):
    for i in range(len(pathList[j])):
        print (pathList[0][i])