from models.Configuration import Configuration
from api.exceptions.ZippedRuntimeException import ZippedRuntimeException

def SanitizeUsernameAndPassword(config: Configuration):
    #The current username and password must be fetched from the environment variables
    _username, _password = config.getUsername(), config.getPassword()

    # If the returned values are null, the following error is shown
    if (_username == 'NULL' or _password == 'NULL'):
        raise ZippedRuntimeException(detail= "You are not currently logged in. Please use the 'login' command or create new credentials")
    return _username, _password