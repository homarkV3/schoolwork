#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void *runner(void *param);

int main(int argc, char *argv[])
{
    pthread_t tid;
    pthread_attr_t attr;
    void *number;
    int i = 0;
    int j = 10;
    if (argc != 2){
        fprintf(stderr, "usage: a.out <integer value>\n");
        return -1;
    }
    if (atoi(argv[1]) < 0){
        fprintf(stderr, "%d must be >= 0\n", atoi(argv[1]));
        return -1;
    }
    pthread_attr_init(&attr);
    pthread_create(&tid,&attr,runner, argv[1]);
    pthread_join(tid, &number);
    printf("%d = ", atoi(argv[1]));
    for(int j = 0; j < sizeof(number); j++){
        if (((int*)number)[j] == 0){
            break;
        } 
        printf(" %d", ((int*)number)[j]);
    }
    printf("\n");
    free(number);
}

void *runner(void *param)
{
    int *oldnum = malloc(10*sizeof(int));
    int num = atoi(param);
    int j = 0;
    while (num%2 == 0){
        oldnum[j] = 2;
        num = num/2;
        j += 1;
    }
    for (int i = 3; i <= sqrt(num); i = i+2){
        while (num%i==0){
            oldnum[j] = i;
            num = num/i;
            j += 1;
        }
    }

    if (num > 2){
        oldnum[j] = num;
    }
    int *buffer = malloc(j * sizeof(int));
    memcpy(buffer, oldnum, sizeof(int) * j);
    return buffer;
    pthread_exit(NULL);
}
