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
template.register_template_library('verbatim_templatetag')
from object import Object

# http://code.google.com/intl/ru/appengine/docs/python/gettingstarted/usingwebapp.html

##################
#
#   Главная форма
#
##################
class MainHandler(webapp.RequestHandler):
    
    def get(self):
		user = users.get_current_user()
		if user:
			template_values = {'username': user.nickname(),
								'logout_url':users.create_logout_url("/")}
			path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
			self.response.out.write(template.render(path, template_values))        
		else:
			self.redirect(users.create_login_url(self.request.uri))

##################
#
#   Основные ajax вызовы
#
##################

class AjaxHandler(webapp.RequestHandler):
    def get(self):
        ret = ''
        # Сперва защита
        user = users.get_current_user()
        if not user:
            ret = "Error"
        else:
            # Потом работа
            do_what = self.request.get('do_what')      
            if do_what == 'user':
                who = int(self.request.get('id'))
                ret = self.getUser(who)
                self.response.headers['Content-Type'] = 'application/json'
                ret = json.dumps(ret,ensure_ascii=False)
            else:
                # Прочие ситуации
                ret =" AJAX rulezzzzz"

        self.response.out.write(ret)


    # получаем данные пользователя по id
    def getUser(self,id):
        u = Object(id);
        ret = u.getall()
        self.response.headers['Content-Type'] = 'application/json'
        return ret


def main():
    application = webapp.WSGIApplication([('/', MainHandler),
    									('/ajax',AjaxHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
