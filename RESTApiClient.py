# *** IMPORTS *** #
import requests


# *** CLASS *** #
class RESTApiClient(object):

    # *** INIT *** #
    def __init__(self,
                 url,
                 params):

        self.url = url
        self.params = params

    # *** API *** #
    def get(self,
            verify):

        return requests.get(url=self.url,
                            verify=verify,
                            params=self.params)

    def post(self,
             verify,
             headers,
             data):

        return requests.get(url=self.url,
                            verify=verify,
                            params=self.params,
                            headers=headers,
                            data=data)
