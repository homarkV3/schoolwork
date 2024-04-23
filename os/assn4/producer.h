#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void factor2pc(struct prodcons *pc, int number);
void *producer(void *data);