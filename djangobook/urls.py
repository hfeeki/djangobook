from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


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
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
