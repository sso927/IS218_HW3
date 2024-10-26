from app.commands import Command
import sys
import logging

class ExitCommand(Command):
    def execute(self):
        logging.info('Exit command registered.')
        sys.exit("Exiting...")
