#from django.conf.urls import patterns, include, url
from django.conf.urls import *

from django.views.generic import list_detail

from mysite.models import Publisher, Author, Book, Person

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mysite.views import author_detail
from mysite.views import books_by_publisher

admin.autodiscover()

publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html',
    #'template_object_name': 'publisher',
}

book_info = {
    'queryset': Book.objects.all(),
    'template_name': 'book.html',
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    ('^hello_inner/', include('djangobook.inner')), #redirect to another url page
    ('^api/', include('api.urls')), #redirect to another url page
    (r'^about/$', direct_to_template, { 'template': 'about.html'}), # direct redirect to about.html page

    (r'^publishers/$', list_detail.object_list, publisher_info),
    (r'^authors/(?P<author_id>\d+)/$', author_detail),
    (r'^books/(\w+)/$', books_by_publisher),
    (r'^books/$', list_detail.object_list, book_info),  #TODO: need to fix it




)
urlpatterns += patterns('mysite.views',
    ('^hello/$', 'hello'),
    ('^hello/$', 'hello'),
    ('^search_form/$', 'search_form'),
    ('^search/$', 'search'),
    ('^contact/$', 'contact_form'),


    ('^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'), # min 1 digit, max 2 digit
    )



# Old url map style
'''
from mysite.views import hello, current_datetime, hours_ahead, search_form, search, contact_form
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangobook.views.home', name='home'),
    # url(r'^djangobook/', include('djangobook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    ('^hello/$', hello),
    ('^search_form/$', search_form),
    ('^search/$', search),
    ('^contact/$', contact_form),


    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead), # min 1 digit, max 2 digit
)

'''