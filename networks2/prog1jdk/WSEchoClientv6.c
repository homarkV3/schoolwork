// CS 2690 Program 1 
// Simple Windows Sockets Echo Client (IPv6)
// Last update: 2/12/19
// Jonathan Kim CS 2690-001 03-02-2021
// Windows 10, Visual Studio 2019 ver 16.9
//
// Usage: WSEchoClientv6 <server IPv6 address> <server port> <"message to echo">
// Companion server is WSEchoServerv6
// Server usage: WSEchoServerv6 <server port>
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

// Minimum required header files for C Winsock program
#include <stdio.h> // for print functions
#include <stdlib.h> // for exit()
#include <winsock2.h>   // for Winsock2 functions
#include <ws2tcpip.h> // adds support for getaddrinfo & getnameinfo for v4+6 name resolution
#include <Ws2ipdef.h> // optional - needed for MS IP Helper

// #define ALL required constants HERE, not inline
// #define is a macro, don't terminate with ';' For example...
#define RCVBUFSIZ 50

// declare any functions located in other .c files here
void DisplayFatalErr(char* errMsg); // writes error message before abnormal termination

void main(int argc, char* argv[])
{
    // Declare ALL variables and structures for main() HERE, NOT INLINE (including the following...)
    WSADATA wsaData; // contains details about WinSock DLL implementation
    struct sockaddr_in6 serverInfo;   // standard IPv6 structure that holds server socket info

    // Verify correct number of command line arguments
    if (argc != 4) {
        fprintf(stderr, "Invalid number of arguments!\n");
        exit(1); // ...and terminate with abnormal termination code (1)
    }

    char* serverIP;
    int serverPort;
    char* msg;
    int mLength;

    serverIP = argv[1];
    serverPort = atoi(argv[2]);
    msg = argv[3];

    mLength = 0;
    while (msg[mLength] != '\0')
    {
        mLength++;
    }

    if (WSAStartup(MAKEWORD(2, 0), &wsaData))
    {
        fprintf(stderr, "Unable to initialize Winsock.\n");
        exit(1);
    }

    int sock;
    sock = socket(AF_INET6, SOCK_STREAM, IPPROTO_TCP);
    if (sock == SOCKET_ERROR)
    {
        DisplayFatalErr("socket() function failed.");
    }
    else
    {
        printf("Socket created successfully.\n");
    }
    struct sockaddr_in6 serverinfo;

    int perrno = -1;
    int v6Only = 0;

    if ((perrno = setsockopt(sock, IPPROTO_IPV6, IPV6_V6ONLY, (char*)&v6Only, sizeof(v6Only))) != 0)
    {
        DisplayFatalErr("setsocket() function failed.");
    }

    memset(&serverInfo, 0, sizeof(serverInfo));
    serverInfo.sin6_family = AF_INET6;
    serverInfo.sin6_port = htons(serverPort);

    inet_pton(AF_INET6, serverIP, &serverInfo.sin6_addr);
    
    int leftOver;
    int bytesSent;
    int offset;
    char rcvBuf[RCVBUFSIZ];
    int bytesRead;

    if (connect(sock, (struct sockaddr*)&serverInfo, sizeof(serverInfo)) < 0)
    {
        DisplayFatalErr("Unable to connect to server");
    }
    else
    {
        printf("Connected to server successfully.\n");
    }

    leftOver = mLength;
    offset = 0;
    while (leftOver)
    {
        bytesSent = send(sock, msg + offset, leftOver, 0);
        if (bytesSent == SOCKET_ERROR)
        {
            DisplayFatalErr("Unable to send message to server");
        }
        else
        {
            offset += bytesSent;
            leftOver -= bytesSent;
        }
    }
    memset(rcvBuf, 0, RCVBUFSIZ);

    leftOver = mLength;
    offset = 0;
    while (leftOver)
    {
        bytesRead = recv(sock, rcvBuf + offset, RCVBUFSIZ - 1 - offset, 0);
        if (bytesRead < 0)
        {
            DisplayFatalErr("Unable to retrieve response from server");
        }
        else if (bytesRead == 0)
        {
            break;
        }
        else
        {
            offset += bytesRead;
            leftOver -= bytesRead;
        }
    }
    // Close the TCP connection (send a FIN) & print appropriate message.
    closesocket(sock);
    printf("Socket closed.\n");

    // Release the Winsock DLL
    WSACleanup();

    exit(0);
}
