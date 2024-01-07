import constants
from typing import List

from parsers import Action_parser
from models import args

def main():
    actions = Action_parser(args, constants.JSON_FILE)

if __name__ == "__main__":
    main()

