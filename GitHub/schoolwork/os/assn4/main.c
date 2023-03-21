
#include "producer.h"
#include "consumer.h"
#include "producer.c"
#include "consumer.c"
#include "main.h"

int main(int argc, char *argv[])
{
    unsigned int n = ((argc == 2) ? atoi(argv[1]) : 1);
    pthread_t t1, t2;

    count = data = consumed = produced = 0;

    if (pthread_mutex_init(&mutex, NULL))
    {
        perror("pthread_mutex_init");
        exit(1);
    }
    if (pthread_cond_init(&control, NULL))
    {
        perror("pthread_cond_init");
        exit(1);
    }
    if (pthread_create(&t1, (pthread_attr_t *)NULL,
                       (void *(*)(void *))producer, (void *)&n))
    {
        perror("pthread_create");
        exit(1);
    }
    if (pthread_create(&t2, (pthread_attr_t *)NULL,
                       (void *(*)(void *))consumer, (void *)&n))
    {
        perror("pthread_create");
        exit(1);
    }

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    fprintf(stdout, "%d %d\n", produced, consumed);
    return (0);
}



