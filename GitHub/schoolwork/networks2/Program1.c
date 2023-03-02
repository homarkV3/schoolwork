// CS 2690 Program 1 
// Simple Windows Sockets Echo Client (IPv6)
// Last update: 2/12/19
// <Your name here> <Your section here> <Date>
// <Your Windows version and Visual Studio version>
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
// ----------------------------------------------------------------------------

// Minimum required header files for C Winsock program
#include <stdio.h>       // for print functions
#include <stdlib.h>      // for exit() 
#include "winsock_wrapper.h"
#include "DisplayFatalErr.c"

// #include <winsock2.h>	 // for Winsock2 functions
// #include <ws2tcpip.h>    // adds support for getaddrinfo & getnameinfo for v4+6 name resolution
// #include <Ws2ipdef.h>    // optional - needed for MS IP Helper

// #define ALL required constants HERE, not inline 
// #define is a macro, don't terminate with ';'  For example...
#define RCVBUFSIZ 50

// declare any functions located in other .c files here
void DisplayFatalErr(char *errMsg); // writes error message before abnormal termination

void main(int argc, char *argv[])   // argc is # of strings following command, argv[] is array of ptrs to the strings
{
	printf("hello");
	// Declare ALL variables and structures for main() HERE, NOT INLINE (including the following...)
	WSADATA wsaData;                // contains details about WinSock DLL implementation
	struct sockaddr_in6 serverInfo = { 0 };	// standard IPv6 structure that holds server socket info

	// Verify correct number of command line arguments, else do the following:
	if (argc < 4){
		printf(stderr, "expected usage: client.exe <IPV6_ADDR> <PORT> \"message\"\n");
		exit(1);
	}
	// fprintf(stderr, "Helpful error message goes here"\n");
	// exit(1);	  // ...and terminate with abnormal termination code (1)
	
	// Retrieve the command line arguments. (Sanity checks not required, but port and IP addr will need
	// to be converted from char to int.  See slides 11-15 & 12-3 for details.)
	char *serverIPaddr = argv[1];
	int serverPort = atoi(argv[2]);
	char *msg = argv[3];

	// Initialize Winsock 2.0 DLL. Returns 0 if ok. If this fails, fprint error message to stderr as above & exit(1).  
	if (WSAStartup(MAKEWORD(2,0), &wsaData) != 0){
		printf(stderr, "WSA startup Failed, so sad, your dad.\n");
		exit(2);
	}
   	// Create an IPv6 TCP stream socket.  Now that Winsock DLL is loaded, 
	// we can signal any errors as shown on next line:
   	int sock = socket(AF_INET6, SOCK_STREAM, IPPROTO_TCP);
	if (sock == INVALID_SOCKET) {
		DisplayFatalErr("socket() function failed.");
	}
	// Display helpful confirmation messages after key socket calls like this:
	printf("Socket created successfully.  Press any key to continue...");
	getchar();     // needed to hold console screen open
	
	// If doing extra credit IPv4 address handling option, add the setsockopt() call as follows...
	// if (perrno = setsockopt(sock, IPROTO_IPV6, IPV6_V6ONLY, (char *)&v6Only, sizeof(v6Only)) != 0)
	//     DisplayFatalErr("setsockopt() function failed.");  
   	
	// Zero out the sockaddr_in6 structure and load server info into it.  See slide 11-15.
	// Don't forget any necessary format conversions.
    serverInfo.sin6_family = AF_INET6;         // address family = IPv6
	serverInfo.sin6_port = htons(serverPort);  // convert int port to ntwk order*
	// Convert cmd line server addr from char to ntwk form, load into sockaddr_in6 
	inet_pton(AF_INET6, serverIPaddr, &serverInfo.sin6_addr);
	// Attempt connection to the server.  If it fails, call DisplayFatalErr() with appropriate message,
	// otherwise printf() confirmation message
    if (connect(sock, (struct sockaddr *) &serverInfo, sizeof(serverInfo)) < 0)
    	DisplayFatalErr("connect() function failed."); 
	// Send message to server (without '\0' null terminator). Check for null msg (length=0) & verify all bytes were sent...
	// ...else call DisplayFatalErr() with appropriate message as before
 
 	// Retrieve the message returned by server.  Be sure you've read the whole thing (could be multiple segments). 
	// Manage receive buffer to prevent overflow with a big message.
 	// Call DisplayFatalErr() if this fails.  (Lots can go wrong here, see slides.)
 	
 	// Display ALL of the received message, in printable C string format.
    
 	// Close the TCP connection (send a FIN) & print appropriate message.

	// Release the Winsock DLL
	
	exit(0);
}
