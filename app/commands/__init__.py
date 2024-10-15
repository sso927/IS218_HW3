from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
    
    def execute_command(self, command_name: str, *args):
        try:
            if command_name in self.commands:
                if len(args) == 0:
                    # Call the execute method with no arguments for commands like "menu"
                    self.commands[command_name].execute()
                else:
                    # Call the execute method with the provided arguments
                    self.commands[command_name].execute(args)
        except KeyError:
            print(f"No such command: {command_name}")