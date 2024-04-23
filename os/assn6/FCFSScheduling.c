// FILE Name: FCFSScheduling.c
#include <stdio.h>
// main function definition
int main()
{
    // To store number of process
    int numberOfProcess;
    // Array to store burst time, waiting time ,turn around time
    int burstTime[20], waitingTime[20], turnAroundTime[20];
    int avgWaitingTime = 0, avgTAT = 0, c, d;
    printf("Enter total number of processes(maximum 20):");
    scanf("%d", &numberOfProcess);

    printf("\nEnter Process Burst Time\n");
    for (c = 0; c < numberOfProcess; c++)
    {
        printf("Process[%d]:", c + 1);
        scanf("%d", &burstTime[c]);
    } // End of for loop
    // Waiting time for first process is 0
    waitingTime[0] = 0;

    // Calculating waiting time
    for (c = 1; c < numberOfProcess; c++)
    {
        waitingTime[c] = 0;
        for (d = 0; d < c; d++)
            waitingTime[c] += burstTime[d];
    } // End of for loop

    printf("\nProcess\t\tBurst Time\tWaiting Time\tTurnaround Time");

    // Calculating turnaround time
    for (c = 0; c < numberOfProcess; c++)
    {
        turnAroundTime[c] = burstTime[c] + waitingTime[c];
        avgWaitingTime += waitingTime[c];
        avgTAT += turnAroundTime[c];
        printf("\nP[%d]\t\t%d\t\t%d\t\t%d", c + 1, burstTime[c], waitingTime[c], turnAroundTime[c]);
    } // End of for loop

    avgWaitingTime /= c;
    avgTAT /= c;
    printf("\n\nAverage Waiting Time: %d", avgWaitingTime);
    printf("\nAverage Turnaround Time: %d", avgTAT);

    return 0;
} // End of main