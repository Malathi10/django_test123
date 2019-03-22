"""
Definition of urls for DjangoAdmin.
"""

from django.contrib import admin
from django.conf.urls import url, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^polls/', include('polls.urls')),


    # Examples:
    # url(r'^$', DjangoAdmin.views.home, name='home'),
    # url(r'^DjangoAdmin/', include('DjangoAdmin.DjangoAdmin.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
