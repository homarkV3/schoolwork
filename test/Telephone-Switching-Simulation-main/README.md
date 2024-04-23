# Telephone-Switching-Simulation

## Topics
* Start Up
  * Whats in the package?
	* Prerequisites to download
	* To start up
* How to Use


## Start Up
To use this program you must have the complete package.

### What’s in the package?
* Main.py [File]
  This serves as the executable to the program
* States [Folder]
  This handles the state changes for the program
* phones.txt [File] - THIS NAME SHOULD NEVER BE CHANGED
  This comes with a set of 20 prebuilt names and numbers, this can be edited to fit the users needs. 

### Prerequisites to download:

* [The latest version of python](https://www.python.org/downloads/) 
* [Python Tabulate Library](https://pypi.org/project/tabulate/) (pip install python)

### To start up
1. Open up the directory with main.py in an IDE that is able to run python OR ensure your CWD is in the sime dir as main.py, and run python3 main.py from the command line.
3. Run main.py program based upon IDE specifications

## How to Use
### phones.txt file
This file is extremely important as it’s what stores the phone name and number combinations. 

Phone numbers are to be 5 digit values followed by a space and up to a 12 alphanumeric name (no spaces). The system will not run if this is not met.

Moreover, there should be no trailing newline characters at the end of the file and will only accept at max 20 phone number name values.

### Console Instructions
When running the main.py file you will be listed a tabulated of all the phones in the system with their Name, Number, and Status. User will also be prompted to choose a phone. 

If you do not see a console screen that prompts for input is a result of the phones.txt file not being formatted correctly.

Inputs to phones can be either a Name or the Phone number.


Once an initial phone is selected you will be prompted with the selected phone information as well as a console of options


#### Call
This command may be used to call another phone in the system. You will be prompted to put in the name or number of another phone.

#### Offhook
This command may be used to place the current phone into an offhook status, which is equivalent to taking the phone off the hook.

#### Onhook
This command may be used to place the current phone into an onhook status, which is equivalent putting the phone on the hook.

#### Transfer
This command may be used to transfer a call. This serves as a cold transfer.

#### Conference
This command may be used to conference a call if you are already on a call with another person. Please remember, you can only have 3 people in a conference call at the same time.

#### Phone Status’
Lists the status’ of all the phones in the system.

#### Switch Phone
This allows the user to switch the active phone they are using. 

#### Quit
This quits the program.
