#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>
#include <sys/types.h>
#include <pthread.h>

pthread_mutex_t mutex;
pthread_cond_t control;
void producer(unsigned int *arg);
void consumer(unsigned int *arg);
unsigned int count, data, consumed, produced;


int
main(int argc, char *argv[]) {
    unsigned int n = ((argc == 2) ? atoi(argv[1]) : 1);
    pthread_t t1, t2;
    
    count = data = consumed = produced = 0;

    if (pthread_mutex_init(&mutex, NULL)) {
    perror("pthread_mutex_init");
    exit(1);
    }
    if (pthread_cond_init(&control, NULL)) {
    perror("pthread_cond_init");
    exit(1);
    }
    if (pthread_create(&t1, (pthread_attr_t *)NULL,
               (void * (*)(void *))producer, (void *)&n)) {
    perror("pthread_create");
    exit(1);
    }
    if (pthread_create(&t2, (pthread_attr_t *)NULL,
               (void * (*)(void *))consumer, (void *)&n)) {
    perror("pthread_create");
    exit(1);
    }
  
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    fprintf(stdout, "%d %d\n", produced, consumed);
    return(0);
}


void producer(unsigned int *arg) {
    unsigned int i, n = *arg;
    for (i=1; i<=n; i++) {
    pthread_mutex_lock(&mutex);
    while (count == 1) {
        pthread_cond_wait(&control, &mutex);
    }
    data = i;
    count = 1;
    pthread_cond_signal(&control);
    pthread_mutex_unlock(&mutex);
    produced++;
    }
}
 

void consumer(unsigned int *arg) {
    unsigned int i = 0, n = *arg;
    while (1) {
    pthread_mutex_lock(&mutex);
    while (count == 0) {
        pthread_cond_wait(&control, &mutex);
    }
    i = data;
    count = 0;
    pthread_cond_signal(&control);
    pthread_mutex_unlock(&mutex);
    consumed++;
    if (i == n) return;
    }
}