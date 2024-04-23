from .state_interface import State


class Onhook(State):
    '''
    docstring
    '''

    def __init__(self):
        self.phone = None

    def onhook(self):
        print("Invalid action. Try again")

    def offhook(self):
        print(f"{self.phone.name} hears dialtone")
        self.phone.transition_state("Offhook")

    def call(self, other_phone):
        print("Invalid action. Try again")

    def receive_call(self, other_phone):
        print(f"{self.phone.name} hears ringing")
        self.phone.transition_state("Ringing", other_phone)

    def conference(self, other_phone):
        print("Invalid action. Try again")

    def transfer(self, other_phone):
        print("Invalid action. Try again")

    def get_status(self):
        return "Onhook"
