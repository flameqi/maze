#include <cstdlib>
#include <iostream>
#include "Queue.h"
#define M 8
#define N 8
using namespace std;
int map[M + 2][N + 2] = { //��ͼ��1Ϊ�����ߣ�0Ϊ����
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
void ShowPath(Queue *qu, int front) //�����ȷ·��
{
    int p = front, p0;
    do
    {
        p0 = p;
        p = qu->data[p].pre;
        qu->data[p0].pre = -1; //����ȷ·����pre��Ϊ-1���Ա��
    } while (p != 0);          //����ѭ�������ҳ���ȷ·��
    cout << "shot path:" << endl;
    // printf("���·��:");
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
    Path(int x0, int y0, int x, int y) //������������Ž�
{
    int i, j, i0, j0,cnt=0; //i,j�洢��ǰ����λ�ã�i0,j0�洢�ҵ���·����λ��
    Box   e;
    //��ǰ����
    Queue *qu;
    InitQueue(qu);
    e.i = x0;
    //�������λ��
    e.j = y0;
    e.pre = -1;
    //���pre����Ϊ-1;
    enQueue(qu, e);
    //������
    map[x0][y0] = -1;       //�߹��ĵ��Ϊ-1����ʾ��������
    while (!QueueEmpty(qu)) //�ӷǿ�ʱѭ��
    {
        deQueue(qu, e);
        //���ӣ���e�洢
        i = e.i; //��¼�õ�����
        j = e.j;
        if (i == x && j == y)
        {
            ShowPath(qu, qu->front);
            //��ӡ·��
            DestroyQueue(qu);
            return true;
        }
        for (int circle = 0; circle < 4; circle++) //������Χ�ķ��飬��������߾ͽ������
        {
            switch (circle) //����˳��Ϊ���ϣ��ң��£���
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
            if (map[i0][j0] == 0) //�ƶ�����λ��
            {
                e.i = i0;
                e.j = j0;
                e.pre = qu->front;
                //��pre��¼���е������±�
                enQueue(qu, e);
                cnt++;
                map[i0][j0] = -1;
                cout <<"i="<< e.i<< "    j="<< e.j<< "   e.pre="<<e.pre<<"  count="<<cnt<<endl;
            }
        }
    }
    DestroyQueue(qu); //����Ϊ�գ�˵���������п��Ե���ķ���������Ҳ������ڣ���Ϊ�޽�
    return false;
}
int  main()
{
    if (!Path(1, 1, 8, 8))
        cout << "noOK";
        // printf("�Թ�����ȷ·��");
    return 0;
}
