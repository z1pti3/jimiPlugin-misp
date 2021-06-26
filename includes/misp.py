import requests
import json
import time
from pathlib import Path

class _misp():

    def __init__(self, apiBaseUrl, apiToken, ca=None, requestTimeout=30):
        self.apiBaseUrl = apiBaseUrl
        self.requestTimeout = requestTimeout
        self.apiToken = apiToken
        self.headers = {
            "Authorization" : "{0}".format(self.apiToken),
            "Content-Type" : "application/json",
            "Accept" : "application/json"
        }
        if ca != None:
            if type(ca) is str:
                self.ca = str(Path(ca))
            elif type(ca) is bool:
                self.ca = ca
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        kwargs["headers"] = self.headers
        if self.ca != None:
            kwargs["verify"] = self.ca
        try:
            url = "{0}/{1}".format(self.apiBaseUrl,endpoint)
            if methord == "GET":
                response = requests.get(url, **kwargs)
            elif methord == "POST":
                kwargs["data"] = json.dumps(data)
                response = requests.post(url, **kwargs)
            elif methord == "DELETE":
                response = requests.delete(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            return 0, "Connection Timeout - {0}".format(e)
        return response.status_code, json.loads(response.text)

    def attributeSearch(self,postData):
        statusCode, response = self.apiCall("attributes/restSearch",methord="POST",data=postData)
        if statusCode == 200:
            return response["response"]["Attribute"]
        else:
            return response

    def attributeSearchValue(self,value):
        data = {
            "value" : value
        }
        statusCode, response = self.apiCall("attributes/restSearch",methord="POST",data=data)
        if statusCode == 200:
            return response["response"]["Attribute"]
        else:
            return response

    def attributeAdd(self,eventId,postData):
        statusCode, response = self.apiCall("attributes/add/{0}/".format(eventId),methord="POST",data=postData)
        if statusCode == 200:
            return response["Attribute"]
        else:
            return response

    def attributeAddValue(self,eventId,value,type):
        data = {
            "value" : value,
            "type" : type
        }
        statusCode, response = self.apiCall("attributes/add/{0}/".format(eventId),methord="POST",data=data)
        if statusCode == 200:
            return response["Attribute"]
        else:
            return response

    def eventGet(self,eventId):
        statusCode, response = self.apiCall("events/view/{0}/".format(eventId))
        if statusCode == 200:
            return response["Event"]
        else:
            return response

    def eventAdd(self,postData):
        statusCode, response = self.apiCall("events/add",methord="POST",data=postData)
        if statusCode == 200:
            return response["Event"]
        else:
            return response
