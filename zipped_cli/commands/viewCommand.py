from unicodedata import name
import click

from api.auth import ReturnUsernameAndPassword
from api.exceptions.ZippedRuntimeException import ZippedRuntimeException
from api.user import SearchFiles, Resource, SearchResource
from models.Configuration import Configuration
from commands.utils import SanitizeUsernameAndPassword
from models.fileModel import ZippedFile

from prettytable import PrettyTable as pt

def _OrganizeResponsesInTable(files):
    tb = pt()

    tb.field_names = ["ID", "File Name", "Owner", "URL"]
    tb.title = "Recieved Files"

    for file in files:
        try: 
            tb.add_row([file.id, "{0}...".format(file.name[0:30]), file.owner, "{0}....".format(file.url)])
        except AttributeError:
            raise ZippedRuntimeException(detail= "The response from the server was malformed. A file's attributes have been corrupted")

    click.secho("Found {0} files to be downloaded. Use the command 'zipped download <url>'".format(len(files)), fg = 'green')
    print(tb)

def _DeserializeResponseToFiles(response):
    try:
        response = response['recievedFiles']
    except KeyError:
        raise ZippedRuntimeException(detail="The server returned an unexpected response. The request could not be fulfilled")
    
    files = []

    for file in response:
        if (isinstance(file, dict)):
            try:
                _file = ZippedFile(file['id'], file['name'], file['url'], file['owner'])
            except KeyError:
                raise ZippedRuntimeException(detail="The server response was missing an attribute")
            if _file:
                files.append(_file)

    return files

@click.command()
@click.option("--count")
@click.pass_context
def file(ctx, count:int = 3):
    config: Configuration = ctx.obj
    _username, _password = SanitizeUsernameAndPassword(config)

    response = SearchResource(
        username=_username, 
        password = _password, 
        resource_path= Resource._RECIEVED_FILES,
        STATUS_404="The server was unable to find your username or password. Please confirm you login information",
        STATUS_500="The server encountered an internal error and was unable to process your request"
    )
    
    files = _DeserializeResponseToFiles(response)
    _OrganizeResponsesInTable(files)

if __name__ == "__main__":
    file()