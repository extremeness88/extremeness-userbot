from typing import Dict, List

class HelpRegistry:
    def __init__(self):
        self.commands: Dict[str, str] = {}

    def register_command(self, command: str, description: str):
        self.commands[command] = description

help_registry = HelpRegistry()