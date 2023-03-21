#include "main.c"
#include "main.h"
#include "consumer.h"
#include "producer.c"
#include "producer.h"

void producer(unsigned int *arg)
{
    unsigned int i, n = *arg;
    for (i = 1; i <= n; i++)
    {
        pthread_mutex_lock(&mutex);
        while (count == 1)
        {
            pthread_cond_wait(&control, &mutex);
        }
        data = i;
        count = 1;
        pthread_cond_signal(&control);
        pthread_mutex_unlock(&mutex);
        produced++;
    }
}