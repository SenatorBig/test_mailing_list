from django.conf.urls import url
from mailsub.views import image_load
urlpatterns = [
    url(r'^image_load/(?P<email_uuid>[a-z0-9\-]+)/$', image_load, name='image_load'),
]
