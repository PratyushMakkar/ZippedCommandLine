
from utils.config import ConfigIO

_USERNAME = "username"
_PASSWORD = "password"
_HOME = "home"

class Configuration(object):
    def __init__(self, _home, _path) -> None:
        self.home = _home
        self.path = _path
        self.configIO: ConfigIO = ConfigIO(path = _path)
        self.username = None
        self.password = None

    def setUsername(self, username:str):
        self.configIO.InsertKey(_USERNAME, username)
        self.username = username
        return self

    def getUsername(self):
        return self.configIO.ReadKey(_USERNAME)

    def setPassword(self, password:str):
        self.configIO.InsertKey(_PASSWORD, password)
        self.password = password
        return self
    
    def getPassword(self):
        return self.configIO.ReadKey(_PASSWORD)

    def setUsernameAndPassword(self, username, password):
        self.setUsername(username).setPassword(password)
        return self
    
    def getUsernameAndPassword(self, username, password):
        return self.getUsername(), self.getPassword()

    def getHome(self):
        return self.configIO.ReadKey(_HOME)
    
    def setHome(self, home):
        self.configIO.InsertKey(_HOME, home)
        self.home = home
        return self
    
    def logOut(self):
        self.configIO.SetUsername("NULL").SetPassword("NULL")
        return self