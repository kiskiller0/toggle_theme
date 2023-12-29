import constants
import subprocess
from helpers import set_theme

for og in constants.PATHS.keys():
    og_file = open(og, "r+")
    alt_file = open(constants.PATHS[og], "r+")

    og_content = og_file.read()
    alt_content = alt_file.read()

    og_file.seek(0)
    alt_file.seek(0)

    og_file.write(alt_content)
    alt_file.write(og_content)

    og_file.close()
    alt_file.close()



current_theme = subprocess.run("dconf read /org/mate/marco/general/theme", shell=True, text=True, capture_output=True).stdout.strip()[1:-1]


theme_set = False # a toggle to know whether the team was set or not

for theme in constants.THEMES["light"]:
    if current_theme == theme["general"]:
        set_theme("dark", constants.THEMES["dark"])
        theme_set = True
        break

if not theme_set:
    set_theme("light", constants.THEMES["light"])


# TODO: use a logger (inform) instead of these print statements
# print(current_theme_general)
# print(current_theme_gtk)

# print("current_theme ({}) == constants.GTK_THEMES['light'] ({})".format(current_theme, constants.GTK_THEMES["light"]))
# print(current_theme == constants.GTK_THEMES["light"])
# print("changing theme from {} to: {}".format(current_theme, theme_choice))
