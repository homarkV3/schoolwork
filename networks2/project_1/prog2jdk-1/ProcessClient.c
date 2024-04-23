// CS 2690 Program 2
// Simple Windows Sockets Echo Client (IPv6)
// Last update: 03/17/21
// Jonathan Kim CS 2690-001 03-17-2021
// Windows 10, Visual Studio 2019 ver 16.9
//
// This program is coded in conventional C programming style, with the 
// exception of the C++ style comments.
//
// I declare that the following source code was written by me or provided
// by the instructor. I understand that copying source code from any other 
// source or posting solutions to programming assignments (code) on public
// Internet sites constitutes cheating, and that I will receive a zero 
// on this project if I violate this policy.
// --------------------------------------------------------------------------

#include <stdio.h>      // for print functions
#include <stdlib.h>     // for exit() 
#include <winsock2.h>    // for WSAGetLastError() 
#include <WS2tcpip.h>
#define CLIENTBUFF 20
void DisplayFatalErr(char* message);
void ProcessClient(SOCKET* clientSock) {
	char clientBuffer[CLIENTBUFF + 1];
	int receiver = 1;
	while (receiver != 0) {
		receiver = recv(clientSock, clientBuffer, CLIENTBUFF, 0);
		if (receiver < 0) {
			DisplayFatalErr("Receive failed.");
		}
		clientBuffer[receiver] = 0;
		send(clientSock, clientBuffer, receiver, 0);
		printf(clientBuffer);
		memset(clientBuffer, '\0', CLIENTBUFF);
		if (receiver < CLIENTBUFF) {
			break;
		}
	}
	printf("\n");
	closesocket(clientSock);
}