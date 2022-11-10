import click

from utils.colour import PrintFiglet, printGreen, printRed, printYellow
from api.user import POSTResource, Resource, UserExists, CreateNewUser
from api.auth import SetUsernameAndPassword
import os

from api.exceptions.ZippedRuntimeException import ZippedRuntimeException
from api.user import SearchResource
from models.Configuration import Configuration

    
@click.command()
@click.option('--user' ,prompt = "Username", help='Your username')
@click.password_option('--password', prompt = "Password", help='Password')
@click.option('--new', is_flag = True)
@click.pass_context
def login(ctx, user: str, password: str, new: bool):

    # Santitize input to ensure its of the type string.
    if (not isinstance(user, str) or not isinstance(password, str)):
        raise ZippedRuntimeException(detail = "The username and password must contain only alphanumeric characters.")
        
    # The '--new' flag specifies if a new user is being created and logged into the terminal
    if (new):
        click.secho("Creating new user with username {0}".format(user), fg = 'yellow')
        
        json = dict(
            username = user,
            password = password
        )
        response = POSTResource(
            json_body= json,
            resource_path= Resource._NEW_USER,
            STATUS_500="The server encountered an internal error and was unable to process your request",
            STATUS_404= "The server was unable to find your username or password. Please confirm you login information",
            STATUS_405= "A user already exists with the given username"
        )
        #CreateNewUser(user, password)

        if (not response):
            raise ZippedRuntimeException(detail="There was an unexpected error while creating a new user. The likely problem is in the server")
        
        click.secho("A new user was created with the username {0}. Your user-session terimates when you close the terminal".format(user), fg = 'green')

    response = SearchResource(
        username=user,
        password = password,
        resource_path= Resource._SEARCH,
        STATUS_500="The server encountered an internal error and was unable to process your request",
        STATUS_404= "The server was unable to find your username or password. Please confirm you login information"
    )
    # If the response returned is not null, a folder 'Zipped' would be created in the desktop and the environement varibales will be set as the user and password
    if (response):
        config: Configuration = ctx.obj
        ctx.obj = config.setUsernameAndPassword(user, password)

        PrintFiglet("{0}".format("ZIPPED"))
        click.secho("Welcome to Zipped {0}. Use -help to get help.".format(user), fg = 'green')
        return
    
    # If the response is not valid, the terminal user is shown an error message. 
    raise ZippedRuntimeException(detail = "Your username or password was incorrect. Please try again")


if __name__ == "__main__":
    login()