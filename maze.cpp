#include <cstdlib>
#include <iostream>
#include "Queue.h"
#define M 8
#define N 8
using namespace std;
int map[M + 2][N + 2] = { //地图，1为不可走，0为可走
    { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
    { 1, 0, 0, 1, 0, 0, 0, 1, 0, 1 },
    { 1, 0, 0, 1, 0, 0, 0, 1, 0, 1 },
    { 1, 0, 0, 0, 0, 1, 1, 0, 0, 1 },
    { 1, 0, 1, 1, 1, 0, 0, 0, 0, 1 },
    { 1, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
    { 1, 0, 1, 0, 0, 0, 1, 0, 0, 1 },
    { 1, 0, 1, 1, 1, 0, 1, 1, 0, 1 },
    { 1, 1, 0, 0, 0, 0, 0, 0, 0, 1 },
    { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 }
};
void ShowPath(Queue *qu, int front) //输出正确路径
{
    int p = front, p0;
    do
    {
        p0 = p;
        p = qu->data[p].pre;
        qu->data[p0].pre = -1; //将正确路径的pre记为-1用以标记
    } while (p != 0);          //利用循环反向找出正确路经
    cout << "shot path:" << endl;
    // printf("最短路径:");
    for (int k = 0; k < MaxSize; k++)
    {
        if (qu->data[k].pre == -1)
        {
            cout << "(" << qu->data[k].i << "," << qu->data[k].j << ")";
            // printf("(%d,%d)->",qu->data[k].i,qu->data[k].j );
            cout << "->";
        }
    }
}
bool
    Path(int x0, int y0, int x, int y) //广度优先找最优解
{
    int i, j, i0, j0,cnt=0; //i,j存储当前方块位置，i0,j0存储找到新路径的位置
    Box   e;
    //当前方块
    Queue *qu;
    InitQueue(qu);
    e.i = x0;
    //设置起点位置
    e.j = y0;
    e.pre = -1;
    //起点pre设置为-1;
    enQueue(qu, e);
    //起点入队
    map[x0][y0] = -1;       //走过的点记为-1，表示不可再走
    while (!QueueEmpty(qu)) //队非空时循环
    {
        deQueue(qu, e);
        //出队，用e存储
        i = e.i; //记录该点坐标
        j = e.j;
        if (i == x && j == y)
        {
            ShowPath(qu, qu->front);
            //打印路径
            DestroyQueue(qu);
            return true;
        }
        for (int circle = 0; circle < 4; circle++) //遍历周围的方块，若方块可走就将其进队
        {
            switch (circle) //遍历顺序为：上，右，下，左
            {
            case 0:
                i0 = i - 1;
                j0 = j;
                break;
            case 1:
                i0 = i;
                j0 = j + 1;
                break;
            case 2:
                i0 = i + 1;
                j0 = j;
                break;
            case 3:
                i0 = i;
                j0 = j - 1;
                break;
            }
            if (map[i0][j0] == 0) //移动至新位置
            {
                e.i = i0;
                e.j = j0;
                e.pre = qu->front;
                //用pre记录队列的数据下标
                enQueue(qu, e);
                cnt++;
                map[i0][j0] = -1;
                cout <<"i="<< e.i<< "    j="<< e.j<< "   e.pre="<<e.pre<<"  count="<<cnt<<endl;
            }
        }
    }
    DestroyQueue(qu); //若队为空，说明遍历所有可以到达的方块后依旧找不到出口，即为无解
    return false;
}
int  main()
{
    if (!Path(1, 1, 8, 8))
        cout << "noOK";
        // printf("迷宫无正确路径");
    return 0;
}
