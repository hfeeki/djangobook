import logging
class MyDebug(object):

    @staticmethod
    def echo(data):
        logging.error(data)

    @staticmethod
    def echo_k(data,k):
        logging.error(strt(k)+" : "+str(data))

    @staticmethod
    def getMethodName(path,i=2):
        w=[]
        w=path.split('/')
        try:
            return w[i]
        except :
            return None


print MyDebug.getMethodName('/api/all_publisher/')
