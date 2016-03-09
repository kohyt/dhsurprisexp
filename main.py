#!/usr/bin/env python
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
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
import urllib

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)


class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Commentk(ndb.Model):
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    datetime = ndb.DateTimeProperty(auto_now_add=True)
    event = ndb.StringProperty()


class Commenta(ndb.Model):
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    datetime = ndb.DateTimeProperty(auto_now_add=True)
    event = ndb.StringProperty()


class Commentt(ndb.Model):
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    datetime = ndb.DateTimeProperty(auto_now_add=True)
    event = ndb.StringProperty()


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Kaleidoscope(webapp2.RequestHandler):
    def get(self):
        comments_query = Commentk.query().order(-Commentk.datetime)
        comments = comments_query.fetch(50)

        user = users.get_current_user()
        if user:
            signinstatus = "Logout"
            url = users.create_logout_url(self.request.uri)
            userinfo = "Logged in as %s".format(user.email())
        else:
            signinstatus = "Login"
            url = users.create_login_url(self.request.uri)
            userinfo = ''

        template_values = {
            'signinstatus': signinstatus,
            'url': url,
            'userinfo': userinfo}

        template = JINJA_ENVIRONMENT.get_template('kaleidoscope.html')
        self.response.write(template.render(template_values))

        # prints the comments below (a div is created for each comment)
        self.response.write("""<div id='comment-area'>""")
        for i in comments:
            if i.event == "http://dhsurprisexp.appspot.com/kaleidoscope":
                if i.author and user:
                    if user.email() == i.author:
                        self.response.write("""<div class="comment"><p><strong>%s (You)</strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
                    else:
                        self.response.write("""<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
                elif i.author:
                    self.response.write(
                            """<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
            else:
                self.response.write(
                        """<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % ('Anonymous', i.content))
        self.response.write("""</div></body></html>""")


class April(webapp2.RequestHandler):
    def get(self):
        comments_query = Commenta.query().order(-Commenta.datetime)
        comments = comments_query.fetch(50)

        user = users.get_current_user()
        if user:
            signinstatus = "Logout"
            url = users.create_logout_url(self.request.uri)
            userinfo = "Logged in as %s".format(user.email())
        else:
            signinstatus = "Login"
            url = users.create_login_url(self.request.uri)
            userinfo = ''

        template_values = {
            'signinstatus': signinstatus,
            'url': url,
            'userinfo': userinfo}

        template = JINJA_ENVIRONMENT.get_template('aprilfools.html')
        self.response.write(template.render(template_values))

        # prints the comments below (a div is created for each comment)
        self.response.write("""<div id='comment-area'>""")
        for i in comments:
            if i.event == "http://dhsurprisexp.appspot.com/aprilfools":
                if i.author and user:
                    if user.email() == i.author:
                        self.response.write("""<div class="comment"><p><strong>%s (You)</strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
                    else:
                        self.response.write("""<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
                elif i.author:
                    self.response.write(
                            """<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
            else:
                self.response.write(
                        """<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % ('Anonymous', i.content))
        self.response.write("""</div></body></html>""")


class Teachers(webapp2.RequestHandler):
    def get(self):
        comments_query = Commentt.query().order(-Commentt.datetime)
        comments = comments_query.fetch(50)

        user = users.get_current_user()
        if user:
            signinstatus = "Logout"
            url = users.create_logout_url(self.request.uri)
            userinfo = "Logged in as %s".format(user.email())
        else:
            signinstatus = "Login"
            url = users.create_login_url(self.request.uri)
            userinfo = ''

        template_values = {
            'signinstatus': signinstatus,
            'url': url,
            'userinfo': userinfo}

        template = JINJA_ENVIRONMENT.get_template('teachersday.html')
        self.response.write(template.render(template_values))

        # prints the comments below (a div is created for each comment)
        self.response.write("""<div id='comment-area'>""")
        for i in comments:
            if i.event == "http://dhsurprisexp.appspot.com/teachersday":
                if i.author and user:
                    if user.email() == i.author:
                        self.response.write("""<div class="comment"><p><strong>%s (You)</strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
                    else:
                        self.response.write("""<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
                elif i.author:
                    self.response.write(
                            """<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % (
                            i.author.email, i.content))
            else:
                self.response.write(
                        """<div class="comment"><p><strong>%s </strong> wrote:%s</p>""" % ('Anonymous', i.content))
        self.response.write("""</div></body></html>""")


class SubmitkForm(webapp2.RequestHandler):
    def post(self):
        comment = Commentk()

        if users.get_current_user():
            comment.author = Author(identity=users.get_current_user().user_id(), email=users.get_current_user().email())
        comment.event = self.request.referer
        comment.content = self.request.get('content')
        comment.put()

        self.redirect(self.request.referer)


class SubmitaForm(webapp2.RequestHandler):
    def post(self):
        comment = Commenta()

        if users.get_current_user():
            comment.author = Author(identity=users.get_current_user().user_id(), email=users.get_current_user().email())
        comment.event = self.request.referer
        comment.content = self.request.get('content')
        comment.put()

        self.redirect(self.request.referer)


class SubmittForm(webapp2.RequestHandler):
    def post(self):
        comment = Commentt()

        if users.get_current_user():
            comment.author = Author(identity=users.get_current_user().user_id(), email=users.get_current_user().email())
        comment.event = self.request.referer
        comment.content = self.request.get('content')
        comment.put()

        self.redirect(self.request.referer)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/submitkform', SubmitkForm),
    ('/submitaform', SubmitaForm),
    ('/submittform', SubmittForm),
    ('/kaleidoscope', Kaleidoscope),
    ('/aprilfools', April),
    ('/teachersday', Teachers)
], debug=True)
