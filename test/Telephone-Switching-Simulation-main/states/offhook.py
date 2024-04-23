from .state_interface import State


class Offhook(State):
    '''
    The phone is off the hook.
    Implements the State abstract class.
    '''
    def __init__(self):
        self.phone = None

    def onhook(self):
        #Phone is back on hook so hears silence.
        self.phone.transition_state("Onhook")
        print(f"{self.phone.name} hears silence")

    def offhook(self):
        print("Invalid action. Try again")

    def call(self, other_phone):
        #Check if other phone is onhook
        if other_phone.is_state("Onhook"):
            other_phone.receive_call(self.phone)

            if other_phone.is_state("Ringing"):
                print(f"{self.phone.name} hears ringback")
                self.phone.transition_state("Calling", other_phone)
            else:
                print(f"{self.phone.name} hears busy")
        else:
            print(f"{self.phone.name} hears busy")

    def receive_call(self, other_phone):
        # busy. other phone should print busy 
        pass

    def conference(self, other_phone):
        print("Invalid action. Try again")

    def transfer(self, other_phone):
        print("Invalid action. Try again")

    def get_status(self):
        return f"Offhook"
