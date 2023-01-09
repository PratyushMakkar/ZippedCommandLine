from calendar import c
from operator import rshift
from urllib import response
from api.exceptions.ZippedRuntimeException import ZippedRuntimeException
from api.user import POSTFileToServer, POSTResource, Resource
import click
from commands.utils import SanitizeUsernameAndPassword
from models.Configuration import Configuration
import json

@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--recipient", multiple = True, type = str)
@click.pass_context
def upload(ctx, file: str, recipient):

    config: Configuration = ctx.obj
    _username, _password = SanitizeUsernameAndPassword(config)
    
    _json = {
        'username': _username,
        'password': _password,
        'filename': file,
        'reciepients': [
            "username15"
        ]
    }

    response = POSTResource(
        json_body= _json,
        resource_path= Resource._META_DATA,
        STATUS_405= "I am not sure about this error LOL",
        STATUS_500="The server encountered an internal error and was unable to process your request",
        STATUS_404= "The server was unable to find your username or password. Please confirm you login information"
    )
    print(response)
    if not response:
        raise ZippedRuntimeException(detail="The server unexpectedly did not return a response")

    try:
        _id = response['_id']
    except KeyError as err:
        raise ZippedRuntimeException(detail="The server could not process the request successfully and returned a malformed response.")

    response = POSTFileToServer(file, _id)

    try:
        response_body = json.loads(response.text)
        download_url = response_body['download_url']
    except KeyError as err:
        raise ZippedRuntimeException(detail="The server returned an unexpcted response without the download URL for the file")

    click.secho("The file has been uploaded and can be found at {0}".format(download_url), fg='green')
           
        