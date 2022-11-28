import os
import sys

sys.path.remove('/usr/lib/python2.7/dist-packages')
sys.path.append('/home/karim/PycharmProjects/test_mailing_list/mailing')
sys.path.append('/home/karim/PycharmProjects/test_mailing_list/venv/lib/python2.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mailing.settings'

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()