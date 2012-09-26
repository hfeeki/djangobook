from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate
from django.core.exceptions import ObjectDoesNotExist

from mysite.models import Publisher, Author, Book, Person
from utility.utility import MyDebug


class CTenHandler(BaseHandler):
    allowed_methods = ('GET')

    def read(self, request):

        #MyDebug.echo(request)
        #MyDebug.echo(request.path)

        path=request.path

        try:
            if MyDebug.getMethodName(path)=='all_publisher':
                if MyDebug.getMethodName(path,3)=='limit':
                    return Publisher.objects.all()[0:int(MyDebug.getMethodName(path,4))]
                return Publisher.objects.all()
            elif MyDebug.getMethodName(path)=='all_book':
                if MyDebug.getMethodName(path,3)=='limit':
                    return Book.objects.all()[0:int(MyDebug.getMethodName(path,4))]
                return Book.objects.all()
            elif MyDebug.getMethodName(path)=='all_author':
                if MyDebug.getMethodName(path,3)=='limit':
                    return Author.objects.all()[0:int(MyDebug.getMethodName(path,4))]
                return Author.objects.all()
            elif MyDebug.getMethodName(path)=='book':
                if MyDebug.getMethodName(path,3)=='title':
                    return {"result_count": Book.count_book_title.title_count(MyDebug.getMethodName(path,4)) }
            elif MyDebug.getMethodName(path)=='person':
                if MyDebug.getMethodName(path, 3)=='male':
                    return Person.men.all()
                if MyDebug.getMethodName(path, 3)=='female':
                    return Person.women.all()
                return Person.people.all()


        except:
            return {"error":"get exception"}


        return {"error":"bad request"}
