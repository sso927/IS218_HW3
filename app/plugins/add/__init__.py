from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.operations import add
import logging

class AddCommand(Command):
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
        
        result = add(num1, num2)
        logging.info('Addition function performed successfully. Good job!')
        print(f"The result of {num1} add {num2} is {result}.")