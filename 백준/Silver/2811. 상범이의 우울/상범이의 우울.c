#include<stdio.h>
#include <stdlib.h>

#define TRUE	1
#define FALSE	0


typedef struct _data
{
    int num;
    int gloomy;
}Data;

typedef struct _node
{
    Data data;
    struct _node* next;
}Node;

typedef struct _list
{
    Node* head;
    Node* cur;
}List;

void ListInit(List* plist);

int LFirst(List* plist, Data* pdata);

void LInsert(List* plist, Data data);

int LNext(List* plist, Data* pdata);
void ListInit(List* plist)
{
    plist->head = NULL;
}

int LFirst(List* plist, Data* pdata)
{
    if (plist->head == NULL)
        return FALSE;

    plist->cur = plist->head;
    *pdata = plist->cur->data;

    return TRUE;
}

void LInsert(List* plist, Data data)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;

    newNode->next = plist->head;

    plist->head = newNode;
}

int LNext(List* plist, Data* pdata)
{
    if (plist->cur->next == NULL)
        return FALSE;

    plist->cur = plist->cur->next;
    *pdata = plist->cur->data;

    return TRUE;
}
int main()
{
    int N;
    scanf("%d", &N);

    int long_gloomy = 0, gloomy = 0;
    List list;
    ListInit(&list);

    for (int i = 0; i < N; i++)
    {
        Data data;
        data.gloomy = 0;
        scanf("%d", &data.num);
        LInsert(&list, data);
        if (data.num < 0) // 최장우울기간을 찾기위한 삼항연산자
        {
            gloomy++;
            long_gloomy = long_gloomy > gloomy ? long_gloomy : gloomy;
        }
        else
        {
            gloomy = 0;
        }
    }

    Data data;
    if (LFirst(&list, &data))
    {
        gloomy = 0;
        int flower = 0, total_flower = 0;   // flower 줘야 될 꽃의 수 , total_flower 준 꽃의 수
        do
        {
            if (data.num < 0)
            {
                gloomy++;
                list.cur->data.gloomy = gloomy;
            }
            else if (gloomy > 0)
            {
                flower = flower > (gloomy * 2) ? flower : (gloomy * 2);
                gloomy = 0;
            }

            if (flower > 0)
            {
                total_flower++;//받은꽃의수
                flower--;
                list.cur->data.num = 0;// 노드의 num이 0이면 꽃을 준날
            }
        } while (LNext(&list, &data));

        int max_flower = 0, long_flower = 0;//long_flower:long gloomy에서 준 꽃의 수, max flower:long flower중 가장 큰것
        if (LFirst(&list, &data))
        {
            flower = 0;
            do
            {
                if (flower > 0)
                {
                    flower--;
                    if ((flower < long_gloomy) && (data.num != 0))
                    {
                        long_flower++;
                    }
                }

                if (data.gloomy == long_gloomy)
                {
                    flower = long_gloomy * 3;
                    max_flower = long_flower > max_flower ? long_flower : max_flower;

                    long_flower = 0;
                }
            } while (LNext(&list, &data));
        }

        if (long_flower > max_flower)
        {
            max_flower = long_flower;
        }

        printf("%d\n", total_flower + max_flower);
    }
}