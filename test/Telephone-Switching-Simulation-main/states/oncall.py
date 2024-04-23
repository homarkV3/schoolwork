from .state_interface import State


class OnCall(State):
    '''
    docstring
    '''
    def __init__(self):
        self.phone = None
        # removed num 1 so the variable can be assigned by transition_state.
        # otherwise we have to go into all the other states and rename them
        # to other_phone1
        self.other_phone = None
        self.other_phone2 = None

    def onhook(self):
        self.phone.transition_state("Onhook")

        self.other_phone.transition_state("Offhook")
        print(f"{self.other_phone.name} hears silence")

        if self.other_phone2 != None:
            self.other_phone2.transition_state("Offhook")
            print(f"{self.other_phone2.name} hears silence")

    def offhook(self):
        print("Invalid action. Try again")

    def call(self, other_phone):
        print("Invalid action. Try again")

    def receive_call(self, other_phone):
        # busy. other phone should print busy 
        pass

    def conference(self, other_phone):

        if self.other_phone2 == None:
            if other_phone.is_state("Onhook"):
                other_phone.state.receive_call(self.phone)

                if other_phone.is_state("Ringing"):
                    print(f"{self.phone.name} hears ringback")
                    
            else:
                print(f"{self.phone.name} hears busy")
        
        else:
            print(f"{self.phone.name} hears denial")


    def transfer(self, other_phone):
        #If in a conference call, transfer is denied
        if self.other_phone2 != None:
            print(f"{self.phone.name} hears denial")
        #If in a regular call, cold transfer
        else:
            #Transition phone you are on a call with to offhook
            self.other_phone.transition_state("Offhook")
            #Phone that you were on a call with calls transfer phone
            self.other_phone.call(other_phone)
            print(f"{self.other_phone.name} transferred to {other_phone.name}")
            self.phone.transition_state("Offhook") #This phone is now offhook

    def get_other_caller(self):
        return self.other_phone

    def get_status(self):
        additional = "" if not self.other_phone2 else f" and {self.other_phone2.name}"
        return f"On a call with {self.other_phone.name}{additional}"
