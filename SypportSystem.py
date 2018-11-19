from InputReader import InputReader
from Responder import Responder

class SupportSystem:
        def __init__(self):
                self.reader = InputReader()
                self.responder = Responder()

        def printWelcome(self):
                print("welcome to imma tech support sytsem")
                print()
                print("please tell us about your problem")
                print("please type 'bye' to exit the system")

        def printGoodbye(self):
                print("Nice talking top you. Bye...")
            
        def start(self):
            finished = False
            self.printWelcome()
            while not finished:
                user_input = self.reader.getInput()
                if user_input.startswith('bye'):
                    finished = True 
                else:
                    response = self.responder.generateResponse
                    print(response)

            self.printGoodbye()