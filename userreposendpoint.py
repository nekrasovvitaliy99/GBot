from endpoint import Endpoint
import requests

class UserReposEndPoint(Endpoint):
    
    error_handler_items = [{'status_code'   : 404,
                                'message'   : 'User not found'}]
    
    def __init__(self, username, token):
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