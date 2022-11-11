import json


class JsonParser:

    def open_json(self, name):
        with open(f'{name}.json', 'r', encoding='utf-8') as fd:
            return json.load(fd)

    def get_json(self, name):
        return self.open_json(name)
