import requests

from errorhandleritem import ErrorHandlerItem

class ErrorHandler:
    
    items = []
    
    def __init__(self, items_list: dict):
        if (isinstance(items_list, list) == False):
            print(type(items_list))
            print(type(list))
            raise Exception('items_list param must be of list type')
        if (len(items_list) == 0):
            raise Exception('items_list must not be empty')
        for item in items_list:
            handler_item = ErrorHandlerItem(item.get('status_code'), item.get('message'))
            self.items.append(handler_item)
    
    def handle(self, request: requests.models.Response):
        for item in self.items:
            item.handle(request)