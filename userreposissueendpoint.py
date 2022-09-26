from endpoint import Endpoint
import requests

class UserReposIssueEndPoint(Endpoint):
    
    error_handler_items = [{'status_code'   : 404,
                                'message'   : 'User not found'}]
    
    def __init__(self, username, repo, title, body, token):
        self.username = username
        self.repo = repo
        self.title = title
        self.body = body
        self.token = token
    
    def getResponse(self):
        json = {"title":self.title, "body":self.body}
        response = requests.post('https://api.github.com/repos/' + self.username + '/' + self.repo + '/issues', json=json, auth=(self.username, self.token))
        return response
    
    def getData(self):
        data = super().getData()
        result = {'issue_created':True}
        return result