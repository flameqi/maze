#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define N 100 
int head  ,rear ,num = 0;
typedef struct node{

    int x , y ;//����
    struct node * next ;

} node_t;
node_t  b[N],way[N] ;//����b���ͼ�¼·������Ľṹ������
void go_map();
void cover() ;
void init();
void print();
node_t * pop();
int a[N][N];//�����ͼ
int  main(){
    while(1){
    memset(a , 0 , sizeof(a));
    int i , j ;
    for( i =1 ; i< 6 ; i ++){
        for( j = 1 ; j < 6; j++) {
                if(scanf("%d",&a[i][j]) == EOF){//�����ͼ
//���ݣ�ע������Ǵ�a[1][1]��ʼ��ģ����潫��ͼ��Ե��1Χ����
                return 0;
            }
        }
    }
    cover();
    init();//��ʼ������
    go_map();
    print();
    }
    return 0;
}
void print(){

    int i;
    for(i = num-1 ; i >= 0 ; i--){//��ӡ���·��
        printf("(%d, %d)\n",way[i].x,way[i].y);
    }
}
void cover(){//��������ͼ��Χ��1Χ��������������

    int i , j ;

    for( i = 0 ; i< 7 ; i++){
        for( j = 0 ;j < 7 ; j++){
            if( i == 0 || i == 6 || j == 0 || j == 6){
                a[i][j] = 1;
            }
        }
    }
}
void init(){//��ʼ������
    head = 0;
    rear = 0;
}
node_t * pop(){//�������г�Ա
    node_t * p ;
    p = &b[head];
    head ++;
    return p ;
}
void record(int x ,int y ,node_t * next){//���߹��ĵ���Ϣ������У�nextΪָ��
//��һ���ڵ����ݵ�ָ��

    b[rear].x = x;
    b[rear].y = y;
    b[rear].next =next ;
    rear ++;
}
void go_map(){//������ͼ
    node_t * temp ;
    record(1,1,NULL);
    while(1){

        if(head >=rear )return ;//����ͷ�Ͷ�β���ʱ���˳�
        temp = pop();

        if( temp -> x == 5 && temp->y == 5){//���ߵ��յ�ʱ����way ��
//���ֱ��淵�ص�����·��

            while(temp != NULL){//����һ�����ݵ�next ָ��ָ��գ�
            //��Ϊ����������ֹ������
                way[num].x = temp->x-1;
                way[num].y =temp->y-1 ;
                num ++ ;
                temp = temp->next;
            }
            return ;
        }
        if(a[temp->x][temp->y - 1]!= 1)//�����ĸ�����ֻҪ����������
        //�ͼ������
        {

            record(temp->x , temp->y -1 ,temp);
            a[temp->x][temp->y - 1] = 1 ;

        }
        if(a[temp->x][temp->y + 1]!=1){

            record(temp->x ,temp->y + 1 ,temp);
            a[temp->x][temp->y + 1] = 1;
        }
        if(a[temp->x-1][temp->y]!= 1){

            record(temp->x- 1 ,temp->y , temp);
            a[temp->x - 1][temp->y] = 1;
        }
        if(a[temp->x + 1][temp->y]!= 1){
            record(temp->x + 1 ,temp->y ,temp);
            a[temp->x + 1][temp->y] = 1;
        }
    }
}