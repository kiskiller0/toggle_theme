import argparse

parser = argparse.ArgumentParser(
        description="Learning Argparse", formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Programmed with Love using Python. Also, Aymen is Gay"
        )

parser.add_argument("--save-theme", choices=["light", "dark"], help="save your current theme to 'themes.json', requires --mode light|dark")
parser.add_argument("--list-themes", action="store_true", help="list available themes")
parser.add_argument("--get-current-theme", action="store_true", help="print current theme info")

args = parser.parse_args()

