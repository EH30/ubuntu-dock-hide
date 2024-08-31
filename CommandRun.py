import os

class CommandRun:
    def runCommand(self, command:str) -> int:
        return os.system(command)
