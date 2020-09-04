import json

from tools.logger import Logger


class JsonImporter:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def write(self):
        try:
            with open(self.filename, 'w') as outfile:
                json.dump(self.data, outfile, indent=2)
                return True
        except FileNotFoundError:
            Logger(__name__).write_error("incorrect json import")
            return False
