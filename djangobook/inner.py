from django.conf.urls import *

urlpatterns = patterns('mysite.views',
    url(r'^multi_urlconf/', 'multi_urlconf' ),
)