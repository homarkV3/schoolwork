#include <pthread.h>

#define SIZE (50)

struct prodcons {
    int buffer [SIZE];
    int count;
    int top;
    int next;
    pthread_mutex_t count_lock;
}

void pc_init(struct prodcons *pc);
int pc_pop(struct prodcons *pc);
void pc_push(struct prodcons *pc, int val);

