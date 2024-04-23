from states.calling import Calling
from states.offhook import Offhook
from states.oncall import OnCall
from states.onhook import Onhook
from states.ringing import Ringing
from tabulate import tabulate
import re


class Phone:

    def __init__(self, name, number):
        self.states = {
            "Calling": Calling(),
            "Offhook": Offhook(),
            "OnCall": OnCall(),
            "Onhook": Onhook(),
            "Ringing": Ringing()
        }

        self.name = name
        self.number = number

        self.transition_state("Onhook")
    
    def transition_state(self, state_name_string, other_phone=None, other_phone2=None):
        self.state = self.states[state_name_string]
        self.state.phone = self

        if other_phone != None:
            self.state.other_phone = other_phone
        
            if other_phone2 != None:
                self.state.other_phone2 = other_phone2
    
    def is_state(self, state_name_string):
        return self.state is self.states[state_name_string]

    def onhook(self):
        self.state.onhook()

    def offhook(self):
        self.state.offhook()

    def call(self, other_phone):
        self.state.call(other_phone)

    def receive_call(self, other_phone):
        self.state.receive_call(other_phone)

    def transfer(self, other_phone):
        self.state.transfer(other_phone)

    def conference(self, other_phone):
        self.state.conference(other_phone)

    def get_status(self):
        return self.state.get_status()


def phoneSelect(phones):
    selected_phone = None
    while selected_phone == None:
        value = input("\nPlease select the phone using Name or Number: ")

        for phone in phones:
            if ((phone.name == value) or (phone.number == value)):
                selected_phone = phone
        if selected_phone == None:
            print("\nA phone with that name or number could not be found, try again!")
    return selected_phone


def is_alphanumeric(string):
    pattern = re.compile('^[a-zA-Z0-9]+$')
    return pattern.match(string) is not None


def phoneIntake(file):
    phones = []
    try:
        with open(file, 'r') as file:
            count = 0
            for line in file:
                count += 1
                if (count > 20):
                    print(
                        "NAME ERROR: Too many Entries, please make sure your phone.txt file contains 20 or less lines")
                    return False
                nline = line.strip().split(" ")

                if (len(nline) > 2):
                    print(
                        "NAME ERROR: Entry is not formatted correctly, please make sure to format in \"Name Phone\" E.g. John 12345")
                    return False

                if (len(nline[1]) > 12):
                    print(
                        f"NAME ERROR: {nline[1]} is longer than 12 characters, please drop a new phone file")
                    return False

                if (not is_alphanumeric(nline[1])):
                    print(
                        f"NAME ERROR: {nline[1]} Must be only alphanumeric characters (A-Z and/or a-z)")
                    return False

                if (len(nline[0]) != 5):
                    print(f"PHONE NUMBER ERROR: {nline[0]} Must be 5 Digits")
                    return False

                try:
                    int(nline[0])
                except ValueError:
                    print(
                        f"PHONE NUMBER ERROR: {nline[0]} must be a 5 digit value e.g 12345")
                    return False

                if (int(nline[0]) > 99999 and int(nline[0]) < 10000):
                    print(
                        f"PHONE NUMBER ERROR: {nline[0]} must be a 5 digit value e.g 12345")
                    return False

                phone = Phone(nline[1], nline[0])
                phones.append(phone)
    except FileNotFoundError:
        print(f"FILE ERROR: File cannot be found. Make sure the file you have is in the same file directory as main.py and has the name of phones.txt")
        return False

    return phones


def main():
    phones = phoneIntake('phones.txt')

    if (phones != False):
        active = True
        print("Welcome to TSP (Telephone Switching Program)")
        tabulatelist = []
        for phone in phones:
            tabulatelist.append(
                [phone.name, phone.number, phone.get_status()])
        print(tabulate(tabulatelist, headers=[
            'NAME', 'NUMBER', 'STATUS'], tablefmt='orgtbl'))
        phone = phoneSelect(phones)
        print(
            f"Phone Successfully Selected:\nName\t | {phone.name}\nNumber\t | {phone.number}\n")
        while active:
            print("\nCommands:")
            print("1: Call\n2: Offhook\n3: Onhook \n4: Transfer \n5: Conference \n6: Phone Status \n7: Switch Phone\n8: Quit")
            value = input(f"Input Command for {phone.name}: ")
            if value == "1":
                phone2 = phoneSelect(phones)
                phone.call(phone2)
            elif value == "2":
                phone.offhook()
            elif value == "3":
                phone.onhook()
            elif value == "4":
                phone2 = phoneSelect(phones)
                phone.transfer(phone2)
            elif value == "5":
                phone2 = phoneSelect(phones)
                phone.conference(phone2)
            elif value == "6":
                tabulatelist = []
                for tabulate_phone in phones:
                    tabulatelist.append(
                        [tabulate_phone.name, tabulate_phone.number, tabulate_phone.get_status()])
                print(tabulate(tabulatelist, headers=[
                    'NAME', 'NUMBER', 'STATUS'], tablefmt='orgtbl'))
            elif value == "7":
                phone = phoneSelect(phones)
                print(
                    f"\nPhone Successfully Switched:\nName\t | {phone.name}\nNumber\t | {phone.number}\n")
            elif value == "8":
                print("Quit")
                active = False
            else:
                print("Invalid Input. Try again")


if __name__ == "__main__":
    main()
