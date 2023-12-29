from random import randint
from typing import List
import subprocess

def set_theme(mode:str, themes:List[dict]):
    theme = themes[randint(0, len(themes) - 1)]

    commands = [
            "dconf write /org/mate/marco/general/theme \"'{}'\"".format(theme["general"]),
            "dconf write /org/mate/desktop/interface/gtk-theme \"'{}'\"".format(theme["gtk"]),
            "dconf write /org/mate/desktop/interface/icon-theme \"'{}'\"".format(theme["icon"]),
            "i3-msg restart"
            ]

    for command in commands:
        try:
            out = subprocess.run(command, shell=True, text=True)
            if out.stderr:
                raise Exception("command {} failed".format(command))
        except Exception as e:
            raise e
