#!/usr/bin/python

import web
from web import form
web.config.debug = True
import json
import md5
import time
import Tool80211

# Testing mode imports
import pdb
import wifiobjects
import random

urls = (
    '/','view_test'
)

class view_test:
    def GET(self):
        

    def POST(self):
        pass

if __name__ == "__main__":
    airmonitor = Tool80211.Airview(options.card)
    airmonitor.start()

    app = web.application(urls,globals())
    app.run()

# WSGI Deployment shit for Apache.
app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

