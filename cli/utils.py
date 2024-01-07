import json

import constants

class Json_handle:
    def __init__(self, fpath):
        self.fpath = fpath

        try:
            fhandle = open(self.fpath, "r")
        except FileNotFoundError:
            choice = input("themes.json not found, create it ?")
            if choice == "yes":
                self.setup_themes_file()
                fhandle = open(self.fpath, "r")

        self.data = json.load(fhandle)
        fhandle.close()

    def write(self, data):
        json.dumps(self.data)

        fhandle = open(self.fpath, "w")
        json.dump(data, fhandle)
        fhandle.close()

    def get_data(self):
        fhandle = open(self.fpath, "r")
        self.data = json.load(fhandle)
        return self.data

    def setup_themes_file(self):
        info = '{"light":[], "dark": []}'
        fh = open(constants.JSON_FILE, "w")
        fh.write(info)
        fh.close()

    def check_themes_file(self):
        try:
            fhandle = open(self.fpath, "r")
        except FileNotFoundError:
            return False

        return True
