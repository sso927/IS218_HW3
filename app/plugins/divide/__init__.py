from decimal import Decimal 
from app.commands import Command
from calculator.operations import divide

class DivideCommand(Command):
    def __init__(self):
        pass

    def execute(self, user_input):
        try:
            num1 = Decimal(user_input[0])
            num2 = Decimal(user_input[1])
        except ValueError:
            print("Please enter valid numbers.")
            return False
        
        result = divide(num1, num2)
        print(f"The result of {num1} divide {num2} is {result}.")

