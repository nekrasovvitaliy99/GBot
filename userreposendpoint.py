from endpoint import Endpoint
import requests

class UserReposEndPoint(Endpoint):
    
    error_handler_items = [{'status_code'   : 404,
                                'message'   : 'User not found'},
                           {'status_code'   : 401,
                                'message'   : 'Bad credentials'}]
    
    def __init__(self, username: str, token: str):
        if (isinstance(username, str) == False):
            raise Exception("username param must be of string type")
        if (isinstance(token, str) == False):
            raise Exception("token param must be of string type")
        if (len(username) == 0):
            raise Exception("lenght of username param must be more than zero")
        if (len(token) == 0):
            raise Exception("lenght of username param must be more than zero")
        self.username = username
        self.token = token
    
    def getResponse(self):
        response = requests.get('https://api.github.com/users/' + self.username + '/repos', auth=(self.username, self.token))
        return response
    
    def getData(self):
        data = super().getData()
        result = {'repos':[]}
        for item in data:
            result['repos'].append(item.get('name'))
        return result