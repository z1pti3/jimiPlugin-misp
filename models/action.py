from os import truncate
import jimi

from plugins.misp.includes import misp

class _mispGetEvent(jimi.action._action):
    apiBaseUrl = str()
    apiToken = str()
    certValidation = True
    caCertFile = str()
    event_id = str()

    def doAction(self,data):
        event_id = jimi.helpers.evalString(self.event_id,{"data" : data["flowData"]})
        apiBaseUrl = jimi.helpers.evalString(self.apiBaseUrl,{"data" : data["flowData"]})
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        if self.caCertFile != "":
            ca = self.caCertFile
        else:
            ca = self.certValidation

        response = misp._misp(apiBaseUrl,apiToken,ca).eventGet(event_id)
        if response:
            return { "result" : False, "rc" : 404, "misp_response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from MISP API" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC ") and value != "":
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_mispGetEvent, self).setAttribute(attr,value,sessionData=sessionData)

class _mispAddEvent(jimi.action._action):
    apiBaseUrl = str()
    apiToken = str()
    certValidation = True
    caCertFile = str()
    event_data = dict()

    def doAction(self,data):
        event_data = jimi.helpers.evalDict(self.event_data,{"data" : data["flowData"]})
        apiBaseUrl = jimi.helpers.evalString(self.apiBaseUrl,{"data" : data["flowData"]})
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        if self.caCertFile != "":
            ca = self.caCertFile
        else:
            ca = self.certValidation

        response = misp._misp(apiBaseUrl,apiToken,ca).eventAdd(event_data)
        if response:
            return { "result" : False, "rc" : 404, "misp_response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from MISP API" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC ") and value != "":
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_mispAddEvent, self).setAttribute(attr,value,sessionData=sessionData)

class _mispAddAttribute(jimi.action._action):
    apiBaseUrl = str()
    apiToken = str()
    certValidation = True
    caCertFile = str()
    event_id = str()
    attribute_data = dict()

    def doAction(self,data):
        event_id = jimi.helpers.evalString(self.event_id,{"data" : data["flowData"]})
        attribute_data = jimi.helpers.evalDict(self.attribute_data,{"data" : data["flowData"]})
        apiBaseUrl = jimi.helpers.evalString(self.apiBaseUrl,{"data" : data["flowData"]})
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        if self.caCertFile != "":
            ca = self.caCertFile
        else:
            ca = self.certValidation

        response = misp._misp(apiBaseUrl,apiToken,ca).attributeAdd(event_id,attribute_data)
        if response:
            return { "result" : False, "rc" : 404, "misp_response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from MISP API" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC ") and value != "":
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_mispAddAttribute, self).setAttribute(attr,value,sessionData=sessionData)

class _mispAddAttributeValue(jimi.action._action):
    apiBaseUrl = str()
    apiToken = str()
    certValidation = True
    caCertFile = str()
    event_id = str()
    attribute_value = str()
    attribute_type = str()

    def doAction(self,data):
        event_id = jimi.helpers.evalString(self.event_id,{"data" : data["flowData"]})
        attribute_value = jimi.helpers.evalString(self.attribute_value,{"data" : data["flowData"]})
        attribute_type = jimi.helpers.evalString(self.attribute_type,{"data" : data["flowData"]})
        apiBaseUrl = jimi.helpers.evalString(self.apiBaseUrl,{"data" : data["flowData"]})
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        if self.caCertFile != "":
            ca = self.caCertFile
        else:
            ca = self.certValidation

        response = misp._misp(apiBaseUrl,apiToken,ca).attributeAddValue(event_id,attribute_value,attribute_type)
        if response:
            return { "result" : False, "rc" : 404, "misp_response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from MISP API" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC ") and value != "":
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_mispAddAttributeValue, self).setAttribute(attr,value,sessionData=sessionData)

class _mispSearchAttribute(jimi.action._action):
    apiBaseUrl = str()
    apiToken = str()
    certValidation = True
    caCertFile = str()
    attribute_data = dict()

    def doAction(self,data):
        attribute_data = jimi.helpers.evalDict(self.attribute_data,{"data" : data["flowData"]})
        apiBaseUrl = jimi.helpers.evalString(self.apiBaseUrl,{"data" : data["flowData"]})
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        if self.caCertFile != "":
            ca = self.caCertFile
        else:
            ca = self.certValidation

        response = misp._misp(apiBaseUrl,apiToken,ca).attributeSearch(attribute_data)
        if response:
            return { "result" : False, "rc" : 404, "misp_response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from MISP API" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC ") and value != "":
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_mispSearchAttribute, self).setAttribute(attr,value,sessionData=sessionData)

class _mispSearchAttributeValue(jimi.action._action):
    apiBaseUrl = str()
    apiToken = str()
    certValidation = True
    caCertFile = str()
    attribute_value = str()

    def doAction(self,data):
        attribute_value = jimi.helpers.evalString(self.attribute_value,{"data" : data["flowData"]})
        apiBaseUrl = jimi.helpers.evalString(self.apiBaseUrl,{"data" : data["flowData"]})
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        if self.caCertFile != "":
            ca = self.caCertFile
        else:
            ca = self.certValidation

        response = misp._misp(apiBaseUrl,apiToken,ca).attributeSearchValue(attribute_value)
        if response:
            return { "result" : False, "rc" : 404, "misp_response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from MISP API" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC ") and value != "":
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_mispSearchAttributeValue, self).setAttribute(attr,value,sessionData=sessionData)