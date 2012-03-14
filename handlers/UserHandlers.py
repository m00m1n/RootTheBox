'''
Created on Mar 13, 2012

@author: moloch
'''

from libs.SecurityDecorators import authenticated
from tornado.web import RequestHandler #@UnresolvedImport

class HomeHandler(RequestHandler):
    
    def initialize(self, dbsession):
        self.dbsession = dbsession
    
    @authenticated
    def get(self, *args, **kwargs):
        ''' Display the default user page '''
<<<<<<< Updated upstream
        self.render('user/user.html', header='User Page')
=======
        self.render('user.html', header='User Page')
>>>>>>> Stashed changes

class SettingsHandler(RequestHandler):
    
    def initialize(self, dbsession):
        self.dbsession = dbsession
    
    def get(self, *args, **kwargs):
        ''' Display the user settings '''
        self.render('user/user_settings.html', header='User Settings')

class LogoutHandler(RequestHandler):
    
    def get(self):
        self.clear_all_cookies()
        self.redirect("/")