from typing import List

import constants
from utils import Json_handle

class Action_parser:
    """Actions take a parsed obj (composition), and executes commands according"""

    # TODO: args should be type notated
    def __init__(self, args, json_file_path):
        self.commands_map = {
                "save_theme": self.save_theme,
                "list_all": self.list_all_themes,
                "list_current": self.list_current_theme,
                "check": self.check_dependencies
                }

        self.args = args
        self.json_handle = Json_handle(constants.JSON_FILE)
        self.exec_commands()

    
    def exec_commands(self):
        for command in self.commands_map.keys():
            if command in self.args.__dict__.keys() and self.args.__dict__[command]:
                self.commands_map[command]()
            

    def save_theme(self):
        theme_color = self.args.__dict__["save_theme"]
        current_json_data = self.json_handle.get_data()
        current_json_data[theme_color].append("new theme!")
        self.json_handle.write(current_json_data)


    def check_dependencies(self):
        for dep in constants.DEPENDENCIES:
            if not shell.command_exists(dep):
                print("requirement {} not available on your system.".format(dep))
                return False

        return True


    def list_all_themes(self):
        # error out if themes.json has invalid json data
        themes = self.json_handle.get_data()

        print("light variants:")
        for theme in themes["light"].keys():
            print(theme)


        print("dark variants:")
        for theme in themes["dark"].keys():
            print(theme)

    def list_current_theme(self):
        current_theme = self.get_current_theme()
        for entry in current_theme.keys():
            print("{}: {}".format(entry, current_theme[entry]))


    def get_current_theme(self) -> dict[str: str]:
        pass

