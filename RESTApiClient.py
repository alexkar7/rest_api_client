# *** IMPORTS *** #
import requests


# *** CLASS *** #
class RESTApiClient(object):

    # *** INIT *** #
    def __init__(self,
                 url):

        self.url = url

    # *** API *** #
    def get(self,
            params):

        return requests.get(self.url,
                            params=params)

    def post(self,
             data):

        return requests.get(self.url,
                            data=data)
