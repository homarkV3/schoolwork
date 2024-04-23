// CS 2690 Program 2 
// Simple Windows Sockets Echo Client (IPv6)
// Last update: 2/12/19
// Jonathan Kim CS 2690-001 03-17-2021
// Windows 10, Visual Studio 2019 ver 16.9
//
// Usage: WSEchoServerv6 <server IPv6 address>
// Companion server is WSEchoClientv6
// 
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
#include <winsock2.h>    // for WSAGetLastError() 
#include <WS2tcpip.h>

void DisplayFatalErr(char* errMsg);
void ProcessClient(SOCKET* clientSock);

int main(int argc, char* argv[]) {

	int sPort = 0;

	switch (argc)
	{
	case 1:
		sPort = 9999;
		break;
	case 2:
		sPort = atoi(argv[1]);
		break;
	case 3:
		printf("Correct usage: WSechoSErverv6.exe [port]\n");
	}


	//Initializethe WinSock DLL.After a successful call to WSAStartup(), handle any errors by callingDisplayFatalErr().
	WSADATA wsaData;
	if (WSAStartup(MAKEWORD(2, 0), &wsaData) != 0) {
		DisplayFatalErr("WSAStartup failed.");
		return 1;
	}
	//Create the server socket.
	SOCKET sSocket = socket(AF_INET6, SOCK_STREAM, IPPROTO_TCP);
	if (sSocket == SOCKET_ERROR)
	{
		DisplayFatalErr("Unable to create socket");
	}
	printf("Socket created successfully.\n");

	struct sockaddr_in6 serverInfo;
	memset(&serverInfo, 0, sizeof(serverInfo)); // zero out the structure
	serverInfo.sin6_family = AF_INET6; // address family = IPv6
	serverInfo.sin6_port = htons(sPort); //convert local port to big endian
	serverInfo.sin6_addr = in6addr_any;

	if (bind(sSocket, (struct sockaddr*)&serverInfo, sizeof(serverInfo)) == SOCKET_ERROR)
	{
		DisplayFatalErr("Unable to bind socket");
	}
	printf("Socket bound successfully to port %d. \n", ntohs(serverInfo.sin6_port));

	if (listen(sSocket, SOMAXCONN) == SOCKET_ERROR)
	{
		DisplayFatalErr("Unable to listen for inbound connections");
	}
	printf("JK's IPv6 echo server is ready for client connection\n");

	struct sockaddr_in6 clientInfo;
	int clientInfoLen = sizeof(clientInfo);

	//Enter a “forever” loop
	for (;;) {
		SOCKET clientSock = accept(sSocket, (struct sockaddr*)&clientInfo, &clientInfoLen);
		char ipv6Array[INET6_ADDRSTRLEN];
		const IN6_ADDR clientAddr = clientInfo.sin6_addr;
		char* goodIp = inet_ntop(AF_INET6, &clientAddr, ipv6Array, sizeof(ipv6Array));
		printf("Processing the client at %s, client port %i\n", goodIp, ntohs(clientInfo.sin6_port));
		ProcessClient(*&clientSock);
	}
}
