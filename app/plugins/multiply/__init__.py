from decimal import Decimal 
from app.commands import Command
from calculator.operations import multiply

class MultiplyCommand(Command):
    def __init__(self):
        pass

    def execute(self, user_input):
        try:
            num1 = Decimal(user_input[0])
            num2 = Decimal(user_input[1])
        except ValueError:
            print("Please enter valid numbers.")
            return False
        
        result = multiply(num1, num2)
        print(f"The result of {num1} multiply {num2} is {result}.")

