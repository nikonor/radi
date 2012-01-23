#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app

# from google.appengine.dist import use_library
# use_library('django', '1.0')
from django.utils import simplejson as json

# http://code.google.com/intl/ru/appengine/docs/python/gettingstarted/usingwebapp.html

class MainUser():
    
    def __init__(self):
        self.data = {}
        self.data['fname'] = "Main"
        self.data['mname'] = "T"
        self.data['lname'] = "User"
        self.data['age'] = 29
        self.data['rus'] = 'юйц'
    
    def get(self,k):
        # print ("get return %s" % self.data[k])
        return self.data[k]

class MainHandler(webapp.RequestHandler):
    def get(self):
    	# получаем главную форму
		user = users.get_current_user()

		if user:
			# self.response.headers['Content-Type'] = 'text/plain'
			# self.response.out.write('Hello, ' + user.nickname())
			template_values = {'username': user.nickname(),
								'logout_url':users.create_logout_url("/")}
			path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
			self.response.out.write(template.render(path, template_values))        
		else:
			self.redirect(users.create_login_url(self.request.uri))

class AjaxHandler(webapp.RequestHandler):
    def get(self):
    	do_what = self.request.get('do_what')
    	ret = ''
    	if do_what == 'mainuser':
            mu = MainUser();
            ret = {}
            ret["name"] = mu.get('fname')+' '+mu.get('mname')+' '+mu.get('lname');
            ret["age"] = mu.get('age');
            ret["rus"] = mu.get('rus')
            # self.response.out.write(ret)
            # json.dumps(self.response, ret)
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps(ret))
    	else:
    		ret = self.nott()
    		self.response.out.write("AJAX rulezzzzz")

    def nott(self):
    	return 'пусто'

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
    									('/ajax',AjaxHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
