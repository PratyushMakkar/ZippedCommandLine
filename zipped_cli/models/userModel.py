class User:
    def __init__(self, user, password):
        self._user=user
        self._password=password

    def getUser(self):
        return self._user
    
    def getPassword(self):
        return self._password

    def setFiles(self, files):
        self._files=files

    def setObjectID(self, id: str):
        self.object_id= id
        return self
        
    def getObjectID(self):
        return self.object_id

    def fromJson(user_object):
        pass

    def toJson(self):
        pass
