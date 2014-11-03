# -*- coding: utf8 -*-
import os
from ConfigParser import SafeConfigParser

class ConfigHandle():
    def __init__(self, configFile):
        self.configFile = configFile or self._getConfigFile()
        self.parser = SafeConfigParser()
        self._open()

    def _getConfigFile(self):
        return os.path.join(os.getcwd(), 'conf', 'weibo.conf')

    def _open(self):
        try:
            self.parser.read(self.configFile)
        except Exception, e:
            print "can't read config file", e

    def get_sections(self):
        return self.parser.sections()

    def get_appid(self):
        return self.parser.get('data', 'APP_ID')

    def set_appid(self, appid):
        self.parser.set('data', 'APP_ID', appid)

    def get_secret(self):
        return self.parser.get('data', 'APP_SECRET')

    def set_secret(self, secret):
        self.parser.set('data', 'APP_SECRET', secret)

    def get_url(self):
        return self.parser.get('data', 'CALLBACK_URL')

    def set_url(self, url):
        self.parser.set('data', 'CALLBACK_URL', url)


    def get_token(self):
        return self.parser.get('oAuth', 'ACCESS_TOKEN')

    def set_token(self, token):
        self.parser.set('oAuth', 'ACCESS_TOKEN', token)

    def get_expires(self):
        return self.parser.get('oAuth', 'EXPIRES_IN')

    def set_expires(self, expires):
        self.parser.set('oAuth', 'EXPIRES_IN', expires)
