
from file_util import File
import json

class JSONFile(File):

    def __init__(self, path):
        super().__init__(path)

    @property
    def text(self):
        return self.pathlib.read_text()

    @property
    def pretty(self):
        return json.dumps(self.dict, indent=4)

    @property
    def dict(self):
        return json.loads(self.text)

    def write_dict(self, _dict):
        text = json.dumps(_dict)
        self.write(text)

    def add_key_value_string(self, key_value: str):

        splits = key_value.split(':')
        key = splits[0]
        value = splits[1]

        _dict = self.dict
        _dict[key] = value
        self.write_dict(_dict)

        return True

    def exists(self):
        return self.pathlib.exists()

    def create(self):
        self.write_dict({})

