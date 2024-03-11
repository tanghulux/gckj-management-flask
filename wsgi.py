import sys

#app's path
sys.path.insert(0,"C:/Users/Administrator/gckj-management")

from mytest import app

#Initialize WSGI app object
application = app
