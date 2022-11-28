from django.conf.urls import url
from mailsub.views import create_mailing_list
urlpatterns = [
    url(r'^create/', create_mailing_list),
]