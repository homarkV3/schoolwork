from .state_interface import State


class Calling(State):
    '''
    This class represents the state of a Phone that is actively 
    dialing and calling another phone.
    Implements the State interface.
    '''
    def __init__(self):
        self.phone = None
        self.other_phone = None

    def onhook(self):
        
        # hang up
        self.phone.transition_state("Onhook")
        print(f"{self.phone.name} hears silence")

        # other phone is not being called anymore
        self.other_phone.transition_state("Onhook")
        print(f"{self.other_phone.name} hears silence")

    def offhook(self):
        print("Invalid action. Try again")

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
        return f"Calling {self.other_phone.name}"
