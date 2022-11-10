import json


class ConfigIO(object):

    def __init__(self, path) -> None:
        self.path = path

    def ReadKey(self, key):
        with open(self.path) as file:
            _json = json.load(file)
            try:
                return _json[key]
            except KeyError as err:
                return None

    def InsertKey(self, key, value):
        with open(self.path, 'r+') as file:
            _json = json.load(file)
            file.seek(0); file.truncate(0)
            _json[key] = value
            file.write(json.dumps(_json, indent=4))
        return self
    
    '''
    def ReadUsername(self):
        with open(self.path) as file:
            _json = json.load(file)
            try:
                return _json['username']
            except KeyError as err:
                return None

    def ReadPassword(self):
        with open(self.path) as file:
            _json = json.load(file)
            try:
                return _json['password']
            except KeyError as err:
                return None

    def SetUsername(self, username):
        with open(self.path, 'r+') as file:
            _json = json.load(file)
            file.seek(0); file.truncate(0)
            _json['username'] = username
            file.write(json.dumps(_json, indent=4))
        return self

    def SetPassword(self, password):
        with open(self.path, 'r+') as file:
            _json = json.load(file)
            file.seek(0); file.truncate(0)
            _json['password'] = password
            file.write(json.dumps(_json, indent=4))
        return self
    
    def ReadHome(self):
        with open(self.path) as file:
            _json = json.load(file)
            try:
                return _json['home']
            except KeyError as err:
                return None
    
    def SetHome(self, home):
        with open(self.path, 'r+') as file:
            _json = json.load(file)
            file.seek(0); file.truncate(0)
            _json['home'] = home
            file.write(json.dumps(_json, indent=4))
        return self
    '''