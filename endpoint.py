import json
from flask import Response
from errorhandler import ErrorHandler

class Endpoint:
    
    def getData(self):
        response = self.getResponse();
        error_handler = ErrorHandler(self.error_handler_items)
        error_handler.handle(response)
        data = response.json()
        return data
    
    def getResultResponce(self):
        data = self.getData()
        response = Response(response = json.dumps(data),
                              status = 200,
                            mimetype = 'application/json')
        return response