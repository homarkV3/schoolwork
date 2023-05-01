// File Name: SJFScheduling.c
#include <stdio.h>

                                                                                                                  int main()
{
    // To store number of process
    int numberOfProcess;
    // Array to store burst time, waiting time ,turn around time
    int burstTime[20], waitingTime[20], turnAroundTime[20], process[20];
    // Loop variables
    int c, d;
    int total = 0, pos, temp;
    float avgWaitingTime = 0, avgTAT = 0;
    printf("Enter number of process:");
    scanf("%d", &numberOfProcess);

    printf("\nEnter Burst Time:\n");
    // Loops till number of processes to accept burst time
    for (c = 0; c < numberOfProcess; c++)
    {
        // Accepts burst time for each process
        printf("Process[%d]: ", c + 1);
        scanf("%d", &burstTime[c]);
        // Contains process number
        process[c] = c + 1;
    } // End of for loop

    // Sorting burst time in ascending order using selection sort
    // Loops till number of process
    for (c = 0; c < numberOfProcess; c++)
    {
        // To store the current index position
        pos = c;
        for (d = c + 1; d < numberOfProcess; d++)
        {
            // Checks burst time of d index position value with burst index position of pos index position value
            // If less then update the pos to d value
            if (burstTime[d] < burstTime[pos])
                pos = d;
        } // End of inner for loop
        // Swapping process for the burst time
        temp = burstTime[c];
        burstTime[c] = burstTime[pos];
        burstTime[pos] = temp;
        // Swapping process for the process number
        temp = process[c];
        process[c] = process[pos];
        process[pos] = temp;
    } // End of outer for loop
    // Waiting time for first process will be zero
    waitingTime[0] = 0;

    // Calculate waiting time for all the processes
    // Loops till number of processes
    for (c = 1; c < numberOfProcess; c++)
    {
        waitingTime[c] = 0;
        // Loops till c value
        for (d = 0; d < c; d++)
            // Calculates waiting time by adding burst time
            waitingTime[c] += burstTime[d];
        // Calculates total waiting time
        total += waitingTime[c];
    } // End of for loop
    // Calculates Average waiting time
    avgWaitingTime = (float)total / numberOfProcess;
    total = 0;

    printf("\nProcess\t Burst Time \tWaiting Time\tTurnaround Time");
    // Loops till number of processes
    for (c = 0; c < numberOfProcess; c++)
    {
        // Calculate turnaround time
        turnAroundTime[c] = burstTime[c] + waitingTime[c];
        total += turnAroundTime[c];
        printf("\np%d\t\t %d\t\t %d\t\t\t%d", process[c], burstTime[c], waitingTime[c], turnAroundTime[c]);
    } // End of for loop
    // Calculates average turnaround time
    avgTAT = (float)total / numberOfProcess;

    printf("\n\nAverage Waiting Time = %.2f", avgWaitingTime);
    printf("\nAverage Turnaround Time = %.2f\n", avgTAT);
} // End of main