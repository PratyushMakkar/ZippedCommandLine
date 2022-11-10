class ZippedFile(object):

    def __init__(self, id, name, url, username) -> None:
        self.id = id
        self.name = name
        self.url = url
        self.owner = username
        

    def setID(self, id):
        self.id = id
        return self

    def setName(self, name):
        self.name = name
        return self

    def setURL(self, url):
        self.url = url
        return self
    
    def setOwner(self, username):
        self.owner = username
        return self
