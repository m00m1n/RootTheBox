# -*- coding: utf-8 -*-
"""
this sets up sqlalchemy.
for more information about sqlalchemy check out <a href="http://www.sqlalchemy.org/">www.sqlalchemy.org</a>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.BaseGameObject import BaseObject

metadata = BaseObject.metadata

# set the connection string here
engine = create_engine('mysql://root@localhost/rtb')
Session = sessionmaker(bind=engine, autocommit=True)

# import the dbsession instance to execute queries on your database
dbsession = Session()

# import your models.
from models.Team import Team
from models.User import User
from models.Box import Box
from models.Action import Action
<<<<<<< HEAD
from models.CrackMe import CrackMe
=======
#from models.Permission import Permission
>>>>>>> 968d323c0b559c43c2be8a53a890192da6109039

# calling this will create the tables at the database
__create__ = lambda: (setattr(engine, 'echo', True), metadata.create_all(engine))

#Bootstrap the database with some shit
def __boot_strap__() :
    import setup.auth
    
    
    
    
