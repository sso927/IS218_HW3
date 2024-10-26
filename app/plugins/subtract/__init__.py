from decimal import Decimal, InvalidOperation 
from app.commands import Command
from calculator.operations import subtract
import logging

class SubtractCommand(Command):
    def __init__(self):
        pass

    def execute(self, user_input):
        try:
            num1 = Decimal(user_input[0])
            num2 = Decimal(user_input[1])
        except (ValueError, InvalidOperation):
            print("Please enter valid numbers. Enter in the format <number1> <number2> <arithmetic operation>")
            logging.error('User input failed. Value error or Invalid operation.')
            return False
        
        result = subtract(num1, num2)
        print(f"The result of {num1} subtract {num2} is {result}.")
        logging.info('Subtraction function performed successfully. Good job!')

