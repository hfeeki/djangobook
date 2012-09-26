from django.conf.urls import *
from piston.resource import Resource

from api.CTen import CTenHandler

urlpatterns = patterns('',

    # Publisher API
    url(r'^all_publisher/$', Resource(CTenHandler)),
    url(r'^all_publisher/xml/$', Resource(CTenHandler), { 'emitter_format': 'xml' }),
    url(r'^all_publisher/limit/\d+/$', Resource(CTenHandler)),
    url(r'^all_publisher/limit/\d+/xml/$', Resource(CTenHandler), { 'emitter_format': 'xml' }),

    # Author API
    url(r'^all_author/$', Resource(CTenHandler)),
    url(r'^all_author/xml/$', Resource(CTenHandler), { 'emitter_format': 'xml' }),
    url(r'^all_author/limit/\d+/$', Resource(CTenHandler)),
    url(r'^all_author/limit/\d+/xml/$', Resource(CTenHandler), { 'emitter_format': 'xml' }),


    # Book API
    url(r'^all_book/$', Resource(CTenHandler)),
    url(r'^all_book/xml/$', Resource(CTenHandler), { 'emitter_format': 'xml' }),
    url(r'^all_book/limit/\d+/$', Resource(CTenHandler)),
    url(r'^all_book/limit/\d+/xml/$', Resource(CTenHandler), { 'emitter_format': 'xml' }),
    url(r'^book/title/[a-z]+/$', Resource(CTenHandler)),

    # Person API
    url(r'^person/$', Resource(CTenHandler)),
    url(r'^person/male/$', Resource(CTenHandler)),
    url(r'^person/female/$', Resource(CTenHandler)),


)


