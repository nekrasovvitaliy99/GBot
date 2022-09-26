import requests

from githubresponseexception import GitHubResponseException

class ErrorHandlerItem:
    
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
    
    def handle(self, request: requests.models.Response):
        if (request.status_code == self.status_code):
            raise GitHubResponseException(404, self.message)