from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.operations import divide
import logging

class DivideCommand(Command):
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
        
        if num2 == 0 :
            print("Error due to divison by zero.")
            logging.error('Divison by zero error from user input.')
            return False 
        
        result = divide(num1, num2)
        print(f"The result of {num1} divide {num2} is {result}.")
        logging.info('Division function performed successfully. Good job!')

