from .state_interface import State


class Ringing(State):
    '''
    This class represents the state of a phone that is actively
    being called by another phone. Implemates the State interface.
    '''
    def __init__(self):
        self.phone = None
        self.other_phone = None

    def onhook(self):
        print("Invalid action. Try again")
        
    def offhook(self):
        # make sure to change other_phone 
        # (the phone that's calling you)
        # to the OnCall state, since it's just
        # hanging out in the Calling state right now.

        # perform the appropriate checks.
        if self.other_phone.is_state("Calling"):
            self.phone.transition_state("OnCall", self.other_phone)
            self.other_phone.transition_state("OnCall", self.phone)
            if self.phone.is_state("OnCall") and self.other_phone.is_state("OnCall"):
                print(f"{self.other_phone.name} and {self.phone.name} are talking")

            else:
                # Error: Unable to connect phone to caller, switch fron OnCall to Offhook
                self.phone.transition_state("Offhook")
                if self.phone.is_state("Offhook"):
                    print(f"{self.phone.name} hears dialtone")
        #conference
        elif self.other_phone.is_state("OnCall"):
            other_phone2 = self.other_phone.state.get_other_caller()

            self.phone.transition_state("OnCall", self.other_phone, other_phone2 )
            self.other_phone.transition_state("OnCall", self.phone, other_phone2)
            other_phone2.transition_state("OnCall", self.phone, self.other_phone)

            print(f"{self.other_phone.name} and {other_phone2.name} and {self.phone.name} are talking")

        # other_phone is in a state other than Calling or OnCall
        # unable to connect to caller/other_phone hung up
        else:
            self.phone.transition_state("Offhook")
            if self.phone.is_state("Offhook"):
                print(f"{self.phone.name} hears dialtone")

    def call(self, other_phone):
        print("Invalid action. Try again")

    def receive_call(self, other_phone):
        # busy. other phone should print busy 
        pass

    def conference(self, other_phone):
        print("Invalid action. Try again")

    def transfer(self, other_phone):
        print("Invalid action. Try again")

    def get_status(self):
        return f"Ringing"
