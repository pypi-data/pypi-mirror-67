import json
from sys import stdout
from typing import Any
from requests import Response
from colored import fg, style

from mdv.markdownviewer import main as mdv


class echo(object):
    message: Any
    expand: bool = False
    list_delimiter: str = '\n'
    indent: int = 4
    color: str = None
    newline: bool = True
    markdown: bool = False

    def __init__(self, message: Any, expand:bool=False,
                 list_delimiter:str='\n', indent:int=4, color:str=None, newline:bool=True, markdown:bool=False):
        self.expand = expand
        self.list_delimiter = list_delimiter
        self.indent = indent
        self.color = color
        self.newline = newline
        self.markdown = markdown
        self._resolve(message)


    def _resolve_response_object(self, response: Response):
        if response.status_code in [200, 201]:
            try:
                return json.dumps(response.json(), indent=4)
            except json.decoder.JSONDecodeError:
                return response.text
        elif response.status_code in [401, 403]:
            return 'Invalid permissions for requests: {response.url}'
        elif response.status_code == 404:
            return f'Unable to find requested resource for: {response.url}'
        elif response.status_code == 400:
            return f'Bad request to: {response.url}'
        elif response.status_code >= 500:
            return f'Server error - {response.url} - {response.status_code} - {response.text}'
        elif response.status_code == None:
            return f'Server error - {response.url} - {response.text}'
        return response.text

    def _resolve_class_object(self, cls: object):
        for attr in dir(cls):
            val = getattr(cls, attr)
            if not attr.startswith('__') and not attr.endswith('__'):
                self.newline = False
                self._resolve(attr + ' ')
                self.newline = True
                self._resolve(val)

    def _resolve(self, message:Any):
        if isinstance(message, str):
            msg = message
            if msg.startswith('#') and self.markdown:
                msg = mdv(md=msg)
        elif isinstance(message, (tuple, list)):
            msg = self.list_delimiter.join(message)
        elif isinstance(message, dict):
            msg = json.dumps(message, indent=self.indent)
        elif isinstance(message, Response):
            msg = self._resolve_response_object(message)
        elif str(type(message)).startswith('<class') and self.expand:
            return self._resolve_class_object(message)
        else:
            msg = str(message)

        if self.newline:
            msg += '\n'

        if self.color:
            msg = f'{fg(self.color)}{msg}{style.RESET}'

        stdout.write(msg)

    def __call__(self, message:Any=None):
        if message:
            self._resolve(message)
        else:
            self._resolve('')
