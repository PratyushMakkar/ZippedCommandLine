from charset_normalizer import detect

import typing as t

from click import ClickException
import click 

from utils.colour import printRed


class ZippedRuntimeException(RuntimeError, ClickException):

    def __init__(self, detail, HTTP_STATUS_CODE = None, *args: object) -> None:
        self.detail = detail
        self.HTTP_STATUS_CODE = HTTP_STATUS_CODE

        assert(isinstance(detail, str))

        super().__init__(*args)

    def show(self, file: t.Optional[t.IO] = None) -> None:
        status_code = self.HTTP_STATUS_CODE
        if (status_code):
            click.echo(click.style(
                text= "ERROR: There was an error with the request and the server returned: {0}. {1}".format(status_code, self.detail), 
                fg='red')
            ) 
            return
        click.echo(click.style(text= "ERROR: {0}".format(self.detail), fg='red'))

    

        