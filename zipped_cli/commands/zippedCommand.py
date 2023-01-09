from cmath import log
from inspect import classify_class_attrs
import json
import os

import click

from commands.loginCommand import login
from commands.uploadCommand import upload
from commands.viewCommand import file
from models.Configuration import Configuration
from utils.colour import printYellow
from commands.downloadCommand import download

directory_name = "Zipped"
_desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
_path = os.path.join(_desktop, directory_name)

def _CreateDesktopFolder():
    if (os.path.isdir(_path)):
        return _path

    printYellow("Creating directory: {0} at location {1}".format(directory_name, _desktop))
    os.mkdir(_path)
    return _path

def ReturnCtxObj():
    config_home = _CreateDesktopFolder()
    path = "{0}/{1}".format(config_home, ".json")
    if (os.path.exists(path)):
        return Configuration(_path, path)
    return 

@click.group()
@click.option("--home", default = _path)
@click.pass_context
def zipped(ctx, home: str):

    # If a home paramater is not specified then a dekstop Zipped folder created is used as home
    config_home = _CreateDesktopFolder()

    # There is a .json file used to store data for the application. 
    path = "{0}/{1}".format(config_home, ".json")

    json_dictionary = {
        'username': "NULL", 
        'password':"NULL",
        'home': home,
        'path': path
    }
    # Creating a json object to be inserted into the config file from the json_dictionary
    json_object = json.dumps(json_dictionary, indent=4)

    if (os.path.exists(path)):
        ctx.obj = Configuration(home, path)
        return

    with open(path, "w") as file:
        ctx.obj = Configuration(home, path)
        file.write(json_object)
        

zipped.add_command(login)
zipped.add_command(file)
zipped.add_command(download)
zipped.add_command(upload)

if __name__ == "__main__":
    cli = click.CommandCollection(sources = [zipped])
    cli()