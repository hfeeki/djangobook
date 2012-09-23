import os

print "PATH:",os.path.realpath(__file__)
print "DIR:",os.getcwd()
PROJECT_DIR=os.path.dirname(__file__)
print PROJECT_DIR
#print os.path.join(PROJECT_DIR, 'templates').replace('\\','/')
print os.path.join(PROJECT_DIR, 'templates').replace('\\','/')

print os.path.realpath(os.path.dirname(__file__))

print os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))