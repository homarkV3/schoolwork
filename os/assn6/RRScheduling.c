// File Name: RRScheduling.c
#include <stdio.h>
    // main function definition
    int
    main()
{

    int counter, j, numberOfProcess, time, remainingProcess, flag = 0, timeQuantum;

    int waitTime = 0, turnAroundTime = 0, ArivalTime[20], burtTime[20], runTime[20];
    // Accepts number of processes from the user
    printf("Enter Total Process:\t ");
    scanf("%d", &numberOfProcess);
    // Assigns number of process to remaining process
    remainingProcess = numberOfProcess;
    // Loops till number of processes
    for (counter = 0; counter < numberOfProcess; counter++)
    {
        // Accepts arrival time and burst time for each process
        printf("Enter Arrival Time and Burst Time for Process Process Number %d :", counter + 1);
        scanf("%d", &ArivalTime[counter]);
        scanf("%d", &burtTime[counter]);
        runTime[counter] = burtTime[counter];
    } // End of for loop
    // Accept time quantum from the user
    printf("Enter Time Quantum:\t");
    scanf("%d", &timeQuantum);

    printf("\n\nProcess\t|Turnaround Time|Waiting Time\n\n");
    // Loops till remaining process
    for (time = 0, counter = 0; remainingProcess != 0;)
    {
        // Checks if the runtime of counter index position value is less than or equals to time quantum
        // and run time counter index position is greater than zero
        if (runTime[counter] <= timeQuantum && runTime[counter] > 0)
        {
            // Increase the time by runtime count index position value
            time += runTime[counter];
            // Set the runtime counter index position value to zero for process finish
            runTime[counter] = 0;
            // Set the flag to one
            flag = 1;
        } // End of if condition
        // Otherwise checks if run time of counter index position value is greater than zero
        else if (runTime[counter] > 0)
        {
            // Subtract quantum from run time counter index position value
            runTime[counter] -= timeQuantum;
            // Increase the time by time quantum
            time += timeQuantum;
        } // End of else if condition
        // Checks if the run time counter index position value is zero and flag is one
        if (runTime[counter] == 0 && flag == 1)
        {
            // Decrease the remaining process by one
            remainingProcess--;
            // Displays process information
            printf("Process[%d]\t | \t%d\t | \t%d\n", counter + 1, time - ArivalTime[counter], time - ArivalTime[counter] - burtTime[counter]);
            // Calculates waiting time for each process
            waitTime += time - ArivalTime[counter] - burtTime[counter];
            // Calculates turn around time for each process
            turnAroundTime += time - ArivalTime[counter];
            // Set the flag to zero for next process
            flag = 0;
        } // End of if condition

        // Checks if counter value is equals to number of process minus one
        if (counter == numberOfProcess - 1)
            // Set the counter value to zero
            counter = 0;
        // Otherwise checks if the arrival time of next counter position value is less than or equals to time
        else if (ArivalTime[counter + 1] <= time)
            // Increase the counter value by one
            counter++;
        // Otherwise
        else
            // Set the counter value to zero
            counter = 0;
    } // End of for loop
    // Displays average waiting and turn around time
    printf("\nAverage Waiting Time= %.2f", waitTime * 1.0 / numberOfProcess);
    printf("\nAvg Turnaround Time = %.2f", turnAroundTime * 1.0 / numberOfProcess);

    return 0;
} // End of main function