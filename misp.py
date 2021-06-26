import jimi

class _misp(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("mispGetEvent","_mispGetEvent","_action","plugins.misp.models.action")
        jimi.model.registerModel("mispAddEvent","_mispAddEvent","_action","plugins.misp.models.action")
        jimi.model.registerModel("mispAddAttribute","_mispAddAttribute","_action","plugins.misp.models.action")
        jimi.model.registerModel("mispAddAttributeValue","_mispAddAttributeValue","_action","plugins.misp.models.action")
        jimi.model.registerModel("mispSearchAttribute","_mispSearchAttribute","_action","plugins.misp.models.action")
        jimi.model.registerModel("mispSearchAttributeValue","_mispSearchAttributeValue","_action","plugins.misp.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("mispGetEvent","_mispGetEvent","_action","plugins.misp.models.action")
        jimi.model.deregisterModel("mispAddEvent","_mispAddEvent","_action","plugins.misp.models.action")
        jimi.model.deregisterModel("mispAddAttribute","_mispAddAttribute","_action","plugins.misp.models.action")
        jimi.model.deregisterModel("mispAddAttributeValue","_mispAddAttributeValue","_action","plugins.misp.models.action")
        jimi.model.deregisterModel("mispSearchAttribute","_mispSearchAttribute","_action","plugins.misp.models.action")
        jimi.model.deregisterModel("mispSearchAttributeValue","_mispSearchAttributeValue","_action","plugins.misp.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        return True
        #if self.version < 0.2:
