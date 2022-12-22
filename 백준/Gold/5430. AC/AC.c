#include <stdio.h>
#include <stdlib.h>
#define TRUE	1
#define FALSE	0

typedef int Data;

typedef struct _node
{
	Data data;
	struct _node * next;
	struct _node * prev;
} Node;

typedef struct _dlDeque
{
	Node * head;
	Node * tail;
} DLDeque;

typedef DLDeque Deque;

void DequeInit(Deque * pdeq);
int DQIsEmpty(Deque * pdeq);

void DQAddFirst(Deque * pdeq, Data data);
void DQAddLast(Deque * pdeq, Data data);

Data DQRemoveFirst(Deque * pdeq);
Data DQRemoveLast(Deque * pdeq);

Data DQGetFirst(Deque * pdeq);
Data DQGetLast(Deque * pdeq);
void DequeInit(Deque * pdeq)
{
	pdeq->head = NULL;
	pdeq->tail = NULL;
}

int DQIsEmpty(Deque * pdeq)
{
	if(pdeq->head == NULL)
		return TRUE;
	else
		return FALSE;
}

void DQAddFirst(Deque * pdeq, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->next = pdeq->head;

	if(DQIsEmpty(pdeq))
		pdeq->tail = newNode;
	else
		pdeq->head->prev = newNode;

	newNode->prev = NULL;
	pdeq->head = newNode;
}

void DQAddLast(Deque * pdeq, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	newNode->prev = pdeq->tail;

	if(DQIsEmpty(pdeq))
		pdeq->head = newNode;		
	else
		pdeq->tail->next = newNode;		

	newNode->next = NULL;
	pdeq->tail = newNode;
}

Data DQRemoveFirst(Deque * pdeq)
{
	Node * rnode = pdeq->head;
	Data rdata = pdeq->head->data;

	if(DQIsEmpty(pdeq))
	{
		printf("Deque Memory Error!");
		exit(-1);
	}

	pdeq->head = pdeq->head->next;
	free(rnode);

	if(pdeq->head == NULL)
		pdeq->tail = NULL;
	else
		pdeq->head->prev = NULL;

	return rdata;
}

Data DQRemoveLast(Deque * pdeq)
{
	Node * rnode = pdeq->tail;
	Data rdata = pdeq->tail->data;

	if(DQIsEmpty(pdeq))
	{
		printf("Deque Memory Error!");
		exit(-1);
	}

	pdeq->tail = pdeq->tail->prev;
	free(rnode);

	if(pdeq->tail == NULL)
		pdeq->head = NULL;
	else
		pdeq->tail->next = NULL;

	return rdata;
}

Data DQGetFirst(Deque * pdeq)
{
	if(DQIsEmpty(pdeq))
	{
		printf("Deque Memory Error!");
		exit(-1);
	}

	return pdeq->head->data;
}

Data DQGetLast(Deque * pdeq)
{
	if(DQIsEmpty(pdeq))
	{
		printf("Deque Memory Error!");
		exit(-1);
	}

	return pdeq->tail->data;
}
int main(void) {

	int tc;
	scanf("%d", &tc);   //테스트케이스 입력
	getchar(); // scanf로 입력을 받으면 버퍼에 \n이 남아있으므로 버퍼를 비워줘야한다.
	for (int i = 0; i < tc; i++) {    
		Deque deq;
		DequeInit(&deq);
		int delete_front = 0;
		int delete_back = 0;
		int num;
		int x = 0;
		int delsum = 0;
		int livedeq = 0;
		int direction = 0;//direction 0이면 reverse안한상태 direction 1이면 reverse한상태
		char a, b;
				while (1) {
			 a = getchar();
			if (a == 'R') {
				if (direction == 0)
					direction = 1;
				else if (direction == 1)
					direction = 0;
			}
			if (a == 'D') {
				if (direction == 0)
					delete_front++;
				if (direction == 1)
					delete_back++;
			}
				if (a == '\n')
					break;
			}
		scanf("%d", &num);
		getchar();//버퍼비우기
		while (1) {//입력할 숫자들을 char형에서 int형으로 바꾼후 덱에 넣어준다.
			b = getchar();
			if (b >= '0'&&b <= '9') {
				x = x * 10 + b - '0';
			}
			else {
				if (x > 0)
					DQAddLast(&deq, x);
				x = 0;
			}

			if (b == ']')
				break;
		}
		getchar();//버퍼비우기
		if (num < (delete_front + delete_back)) {//입력받은숫자보다 D함수를 더많이 사용하면 error출력
			printf("error\n");
		}
		if (num == (delete_front + delete_back)) {
			printf("[]\n");
		}
		if (direction == 0&&num>(delete_front+delete_back)) { //방향이 바뀌지않은상태
			printf("[");
			while (delete_front != 0) {
				DQRemoveFirst(&deq);
				delete_front--;
				delsum++;
			}
			while (delete_back != 0) {
				DQRemoveLast(&deq);
				delete_back--;
				delsum++;
			}
			livedeq = num - delsum; 
			while (livedeq != 1) {
					printf("%d,", DQRemoveFirst(&deq));
					livedeq--;
			}
			printf("%d]\n", DQGetFirst(&deq));
		}

		if (direction == 1&&num>(delete_front+delete_back)) { //방향이 바뀐상태
			printf("[");
			while (delete_front != 0) {
				DQRemoveFirst(&deq);
				delete_front--;
				delsum++;
			}
			while (delete_back != 0) {
				DQRemoveLast(&deq);
				delete_back--;
				delsum++;
			}
			livedeq = num - delsum;
			while (livedeq != 1) {
					printf("%d,", DQRemoveLast(&deq));
					livedeq --;
			}
			printf("%d]\n", DQGetLast(&deq));
			
		}
		

	}
	
	
	return 0;
}