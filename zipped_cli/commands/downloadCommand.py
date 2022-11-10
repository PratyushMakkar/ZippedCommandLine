import click

import os

from requests import request
import requests

from api.auth import ReturnUsernameAndPassword
from api.exceptions.ZippedRuntimeException import ZippedRuntimeException
from api.user import SearchFiles
from models.Configuration import Configuration
from commands.utils import SanitizeUsernameAndPassword

from urllib.parse import urlparse
from os.path import splitext, basename

@click.command()
@click.option("--location", default = None)
@click.argument('url')
@click.pass_context
def download(ctx, location, url):

    if (not url):
        raise ZippedRuntimeException(detail= "A URL for the file must be specified")

    config: Configuration = ctx.obj
    _home = config.getHome()
    
    if (location):
        _home = location

    if (not os.path.isdir(_home)):
        raise ZippedRuntimeException(detail= "The directory: {0} does not exist or could not be accessed".format(_home))
    
    disassembled = urlparse(url)
    filename, file_ext = splitext(basename(disassembled.path))
    file_path = "{0}/{1}".format(_home, filename + file_ext)

    try:
        r = requests.get(url, allow_redirects=True)
    except ConnectionError as err:
        raise ZippedRuntimeException(detail="A connection to the website could not be made. Please check your internet connection.")
    except Exception as err:
        raise ZippedRuntimeException(detail="There was an unknown error while trying to download the file. Please check the url specified")

    with open(file_path, 'wb') as file:
        file.write(r.content)

    click.secho("File successfully downloaded in folder :{0}".format(_home), fg = 'green')

if __name__ == "__main__":
    download()