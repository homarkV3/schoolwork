#include "main.c"
#include "main.h"
#include "consumer.h"
#include "producer.c"
#include "producer.h"

void consumer(unsigned int *arg)
{
    unsigned int i = 0, n = *arg;
    while (1)
    {
        pthread_mutex_lock(&mutex);
        while (count == 0)
        {
            pthread_cond_wait(&control, &mutex);
        }
        i = data;
        count = 0;
        pthread_cond_signal(&control);
        pthread_mutex_unlock(&mutex);
        consumed++;
        if (i == n)
            return;
    }
}