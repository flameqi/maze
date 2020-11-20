#encoding = utf-8
import copy#列表和字典需要的深度复制
#迷宫数组
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



XLEN=6#迷宫宽度-1
YLEN=8#迷宫高度-1
steps=[['0' for col in range(XLEN+1)] for row in range(YLEN+1)]#建立痕迹数组
startP=[3,0]#起点坐标
endP=[3,8]#终点坐标
#构建节点
node={'x':startP[0],'y':startP[1],'pre':-1,'dir':{'up':0,'down':0,'left':0,'right':0,'main':0},'index':0}
#构建所有节点队列，并压入起点
pathList={'node':[{'x':startP[0],'y':startP[1],'pre':-1,'dir':{'up':0,'down':1,'left':0,'right':0},'index':0,'main':0}],'front':-1,'rear':-1}# index 1:x index 2:y index 3:re
pathList['rear']+=1#起点已经压入队列，所以后节点要加1
steps[node['y']][node['x']]='1'#起点留下痕迹
preX=-1
preY=-1
index=0
dir={'up':0,'down':0,'left':0,'right':0}
print (puzzle)
print("#############################")


while (pathList['front']!=pathList['rear']):
    
        #node['dir']={'up':0,'down':0,'left':0,'right':0}
        pathList['front']+=1#把队列中下一个节点做为前节点
        node=copy.deepcopy(pathList['node'][pathList['front']])#获取前节点
        if (node['x']>=0 and node['x']<XLEN):
            if(puzzle[node['y']][node['x']+1]==0):
                node['dir']['right']=1
            else:
                node['dir']['right']=0
        if (node['y']>=0 and node['y']<YLEN):
            if(puzzle[node['y']+1][node['x']]==0):
                node['dir']['down']=1
            else:
                node['dir']['down']=0
        if (node['x']>=1 and node['x']<=XLEN):
            if(puzzle[node['y']][node['x']-1]==0):
                node['dir']['left']=1
            else:
                node['dir']['left']=0
        if (node['y']>=1 and node['y']<=YLEN):
            if(puzzle[node['y']-1][node['x']]==0):
                node['dir']['up']=1
            else:
                node['dir']['up']=0
        pathList['node'][pathList['front']]=copy.deepcopy(node)
########################以上是判断当前节点四周是否可通过#####################################

        preX=node['x']
        preY=node['y']

        for dir in node['dir']:
            if (node['dir'][dir]==1 ):
                if(dir=='up'):
                    node['x']=preX
                    node['y']=preY-1
                if(dir=='down'):
                    node['x']=preX
                    node['y']=preY+1
                if(dir=='left'):
                    node['x']=preX-1
                    node['y']=preY
                if(dir=='right'):
                    node['x']=preX+1
                    node['y']=preY
############################以上是移动当前节点到可通过的新位置######################################
            if(node['x']>=0 and node['x']<=XLEN and node['y']>=0 and node['y']<=YLEN):#判断当前节点是不是在迷宫之外
                if (steps[node['y']][node['x']]=='0'):#判断当前节点是不是已走过。
                    pathList['rear']+=1#后节点加1是为压入新节点做准备
                    node['pre']=pathList['front']#从队列里把前节点的索引值给节点当中指向的前节点。
                    index+=1
                    node['index']=index
                    pathList['node'].append(copy.deepcopy(node))#压入新探索出来的节点
                    # pathList['node'][pathList['rear']]=node
                    steps[node['y']][node['x']]='1'#为新节点留下痕迹


k=-1
# k=len(pathList['node'])-1#开始回溯最佳路线
xxx=-1
yyy=-1
endNodeIndex=0
for p in pathList['node']:
    if (p['x']==endP[0] and p['y']==endP[1]):#匹配终点
        xx=p['x']
        yy=p['y']
        endNodeIndex=p['index']
        p['main']=1
        k=p['pre']
        xxx=pathList['node'][k]['x']
        yyy=pathList['node'][k]['y']
        pathList['node'][k]['main']=1
        if ((xxx-xx)==0 and (yyy-yy)<0 ):
            steps[yy][xx]='↑'
        if ((xxx-xx)==0 and (yyy-yy)>0 ):
            steps[yy][xx]='↓'
        if ((xxx-xx)>0 and (yyy-yy)==0 ):
            steps[yy][xx]='→'
        if ((xxx-xx)<0 and (yyy-yy)==0 ):
            steps[yy][xx]='←'

while (k>-1):
    xx=pathList['node'][k]['x']
    yy=pathList['node'][k]['y']
    k=pathList['node'][k]['pre']
    pathList['node'][k]['main']=1
    xxx=pathList['node'][k]['x']
    yyy=pathList['node'][k]['y']
    if ((xxx-xx)==0 and (yyy-yy)<0 ):
        steps[yy][xx]='↑'
    if ((xxx-xx)==0 and (yyy-yy)>0 ):
        steps[yy][xx]='↓'
    if ((xxx-xx)>0 and (yyy-yy)==0 ):
        steps[yy][xx]='→'
    if ((xxx-xx)<0 and (yyy-yy)==0 ):
        steps[yy][xx]='←'
for j in range(len(pathList['node'])):#输出整个队列也就是输出搜索过程
    print (pathList['node'][j])
for s in steps:#输出最佳路线
    print (s)


########################以下是找出无人机探索的所有节点的最短路径。以回溯出最佳路线为基础，最佳路线是主分支。######################
uavs=[{'x':0,'y':0,'pPre':0,'pIndex':0,'main':0,'pNext':[],'pYet':[]}]

pIndex=0#
uIndex=0#

uavs.append({\
    'x':pathList['node'][pIndex]['x'],\
    'y':pathList['node'][pIndex]['y'],\
    'pPre':pathList['node'][pIndex]['pre'],\
    'pIndex':pathList['node'][pIndex]['index'],\
    'main':pathList['node'][pIndex]['main'],\
    'pNext':[],\
    'pYet':[]})
uIndex+=1

sub=False
subEnd=0
subStep=0
while (True):
    
    for p1 in pathList['node']:#历遍队列，找出与无人机节点的index相等的pre，压入pNext列表
        if (p1['pre']==uavs[uIndex]['pIndex']):
            if (not p1['index'] in uavs[uIndex]['pNext']):
                uavs[uIndex]['pNext'].append(p1['index'])
    if (len(uavs[uIndex]['pNext'])>1):#如果无人机队列当前节点在路径队列的下一个节点数大于1那说明当前节点是分叉的。准备进入副分支的计步变量。
        sub=True
        subStep=0
    if (len(uavs[uIndex]['pNext'])!=0):#如果无人机队列的当前节点在路径队列中有下一个节点
        for ns in uavs[uIndex]['pNext']:#历遍查找所有的子节点
            if(not (pathList['node'][ns]['index'] in uavs[uIndex]['pYet'])):#如果不是已经走过的节点则加入到无人机队列，
                if(pathList['node'][ns]['main']==0 ):#如果是分支节点直接压加无人机队列，如果不是则有没有其他没走过的。
                    if (sub):
                        subStep+=1
                    uavs.append({\
                        'x':pathList['node'][ns]['x'],\
                        'y':pathList['node'][ns]['y'],\
                        'pPre':pathList['node'][ns]['pre'],\
                        'pIndex':pathList['node'][ns]['index'],\
                        'main':pathList['node'][ns]['main'],\
                        'pNext':[],\
                        'pYet':[]})
                    uavs[uIndex]['pYet'].append(ns)#给母节点中的子节点列表写已走的标记
                    uIndex+=1
                    break#跳出历遍到while(true)，把当前节点做为无人机队列里的最后一个节点继续
                else:
                    if ((len(uavs[uIndex]['pNext'])-len(uavs[uIndex]['pYet']))>1):#如果存在没走过节点的则跳过本次循环，继续历遍查找
                        continue
                if (sub):
                    subStep+=1
                uavs.append({\
                    'x':pathList['node'][ns]['x'],\
                    'y':pathList['node'][ns]['y'],\
                    'pPre':pathList['node'][ns]['pre'],\
                    'pIndex':pathList['node'][ns]['index'],\
                    'main':pathList['node'][ns]['main'],\
                    'pNext':[],\
                    'pYet':[]})
                uavs[uIndex]['pYet'].append(ns)#给无人机队列的母节点中的子节点列表写已走的标记
                uIndex+=1
                break   
            else:
                continue#如果走过继续历遍查找。
    else:#如果没有子节点则回退
        subEnd=uIndex#记录当前分支端点的索引值
        returnStep=1
        while (returnStep<=subStep):
            uavs.append(copy.deepcopy(uavs[subEnd-returnStep]))#把回退的节点复制追加给无人机队列
            uIndex+=1#增加无人机队列的最后一个端点的索引值。
            returnStep+=1#退回一步
        sub=False
    if(uavs[len(uavs)-1]['pIndex']==endNodeIndex):#如果到终点则结束。
        break
for ww in uavs:
    print (ww)
