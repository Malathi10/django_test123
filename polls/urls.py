"""
Definition of urls for DjangoAdmin.
"""

from django.conf.urls import url
from . import views
from polls.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$',views.index, name='index'),

]
