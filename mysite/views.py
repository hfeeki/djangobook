
from django.http import Http404, HttpResponse

import datetime
import logging
from django.shortcuts import render_to_response

'''
    Hello world response
'''
def hello(request):
    return HttpResponse("Hello world")

'''
    Generate HTTP response
'''
def current_datetime_old(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

'''
    Generate HTTP response via template
'''
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

'''
    Generate HTTP response via template
'''
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('current_datetime.html', {'current_date': dt})

'''
    Generate HTTP response here
'''
def hours_ahead_old(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)