import subprocess

class ToolAdapter:
    command = ""
    args = []
    name = ""

    def __init__(self, command, args, name):
        self.command = command
        self.args = args
        self.name = name

    def exec():
        return subprocess.run([command, *args])