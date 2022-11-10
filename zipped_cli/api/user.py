import os
from pkg_resources import require
import requests
from requests import status_codes
from dotenv import load_dotenv
from requests.exceptions import ConnectionError
import json

from api.exceptions.ZippedRuntimeException import ZippedRuntimeException

load_dotenv()
SERVER_URL = os.environ.get("SERVER_HOST")

class Resource:
    _SEARCH = "search"
    _RECIEVED_FILES = "recievedFiles"
    _NEW_USER = "user/"
    _META_DATA = "files/meta_data"
    _UPLOAD = "files"

def POSTFileToServer(filepath: str, id: str):
    url = "{0}/{1}?id={2}".format(SERVER_URL, Resource._UPLOAD, id)

    with open(filepath, 'rb') as file:
        files = {'file' : file}
        response = requests.post(url, files=files)  
    return response
    

def SearchResource(username, password, 
    resource_path: str, 
    STATUS_500: str, 
    STATUS_404: str, 
    STATUS_200 = None
):
    json_body = dict(
        username= username,
        password = password
    )
    url = "{0}/user/{1}".format(SERVER_URL, resource_path)

    try:
        response = requests.get(url=url,
           json= json_body
        )
    except ConnectionError as err:
        raise ZippedRuntimeException(detail= "There was a connection error. Please check your connection")

    match response.status_code:
        case 404:
            raise ZippedRuntimeException(HTTP_STATUS_CODE= 404, detail= STATUS_404)
        case 500:
            raise ZippedRuntimeException(HTTP_STATUS_CODE=500, detail= STATUS_500)
        case 200:
            if (STATUS_200):
                STATUS_200()
            return json.loads(response.text)
        
    return None

def POSTResource(json_body, 
    resource_path: str, 
    STATUS_500: str, 
    STATUS_404: str, 
    STATUS_405: str,
    STATUS_200 = None
):
    
    url = "{0}/{1}".format(SERVER_URL, resource_path)

    try:
        response = requests.post(url=url,
           json= json_body
        )
    except ConnectionError as err:
        raise ZippedRuntimeException(detail= "There was a connection error. Please check your connection")

    match response.status_code:
        case 404:
            raise ZippedRuntimeException(HTTP_STATUS_CODE= 404, detail= STATUS_404)
        case 500:
            raise ZippedRuntimeException(HTTP_STATUS_CODE=500, detail= STATUS_500)
        case 405: 
            raise ZippedRuntimeException(HTTP_STATUS_CODE=500, detail= STATUS_405)
        case 200:
            if (STATUS_200):
                STATUS_200()
            return json.loads(response.text)
        
    return None
    
    
def UserExists(username, password) -> object: 

    json_body = dict(
        username= username,
        password = password
    )
    url = "{0}/user/search".format(SERVER_URL)
        
    try:
        response = requests.get(url=url,
           json= json_body
        )
    except ConnectionError as err:
        raise ZippedRuntimeException(detail= "There was a connection error. Please check your connection")
    
    match response.status_code:
        case 404:
            raise ZippedRuntimeException(HTTP_STATUS_CODE= 404, detail= "The server was unable to find your username or password. Please confirm you login information")
        case 500:
            raise ZippedRuntimeException(HTTP_STATUS_CODE=500, detail= "The server encountered an internal error and was unable to process your request")
        case 200:
            return json.loads(response.text)
    
    return None

def CreateNewUser(user: str, password:str):
    return None

def SearchFiles(username: str, password: str):

    json_body = dict(
        username= username,
        password = password
    )

    resource_url = "{0}/user/recievedFiles".format(SERVER_URL)

    response = requests.get(
        url= resource_url,
        json=json_body
    )

    match response.status_code:
        case 404:
            raise ZippedRuntimeException(HTTP_STATUS_CODE= 404, detail= "The server was unable to find your username or password. Please confirm you login information")
        case 500:
            raise ZippedRuntimeException(HTTP_STATUS_CODE=500, detail= "The server encountered an internal error and was unable to process your request")
        case 200:
            return response.text
