#-*- coding: utf-8 -*-

import sys
from weibo import APIClient
from config import ConfigHandle


class WeiboAgent():
    def __init__(self, key=None, secret=None, redirect_uri=None, configFile=''):
        self.parser = ConfigHandle(configFile)

        self.app_key = key or self.parser.get_appid()
        self.app_secret = secret or self.parser.get_secret()
        self.callback_url = redirect_uri or self.parser.get_url() 
        self.client = APIClient(app_key=self.app_key, app_secret=self.app_secret,\
                redirect_uri=self.callback_url)

        self.access_token = self.parser.get_token()
        self.expires_in = self.parser.get_expires()

    def authorize(self):
        url = self.client.get_authorize_url()
        
        try: 
            self.client.set_access_token(self.access_token, self.expires_in)
        except:
            code = raw_input("Please put the url in your Chrome and get the code->\n %s:\n" % url)
            r = self.client.request_access_token(code)
            self.access_token = r.access_token or self.access_token
            self.expires_in = r.expires_in or sel.expires_in
            self.parser.set('oAuth', 'ACCESS_TOKEN', r.access_token)
            self.parser.set('oAuth', 'EXPIRES_IN', r.expires_in)
            self.client.set_access_token(self.access_token, self.expires_in)

    def get_recent_statuses(self, num=20):
        return  self.client.statuses.user_timeline.get(count=num)

    def get_home_statuses(self, num=20):
        return  self.client.statuses.home_timeline.get(count=num)

    def get_public_statuses(self, num=20):
        return  self.client.statuses.public_timeline.get(count=num)

    def get_friends_statuses(self, num=20):
        return  self.client.statuses.friends_timeline.get(count=num)

    def post_status(self, msg):
        try:
            self.client.statuses.update.post(status=msg)
            return True
        except Exception, e:
            return False

    def post_status_with_pic(self, msg, pic):
        try:
            self.client.statuses.upload.post(status=meg, pic=open(pic))
            return True
        except Exception, e:
            return False

    def get_uid(self):
        return self.client.account.get_uid.get()
