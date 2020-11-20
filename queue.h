#pragma once
#define MaxSize 100
typedef struct
{
    int i, j;
    //方块在地图中的位置
    int pre; //该路径中上一个方块在队列中的下标
}Box ;
//方块类型
typedef struct
{
    Box data[MaxSize];
    int front, rear;
}Queue;
//用于存放路径的队列
void InitQueue(Queue *&q)
{
    q = (Queue *)malloc(sizeof(Queue));
    q->front = q->rear = -1;
}
void DestroyQueue(Queue *&q)
{
    free(q);
}
bool QueueEmpty(Queue *q)
{
     return  (q->front == q->rear);
}
bool enQueue(Queue *&q, Box e)
{
    if (q->rear == MaxSize - 1)
         return false;
    q->rear++;
    q->data[q->rear] = e;
     return true;
}
bool deQueue(Queue *&q, Box  &e)
{
    if (q->rear == q->front)
         return false;
    q->front++;
    e = q->data[q->front];
     return true;
}
