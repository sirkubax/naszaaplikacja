#!/usr/bin/python

activate_this = '/var/www/FLASKAPPS/helloworldapp/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0,"/var/www/FLASKAPPS/")
from helloworldapp import app as application
