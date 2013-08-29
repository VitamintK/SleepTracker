"""Simple sleep schedule tracker for curiousity purposes"""
from datetime import datetime
import pickle

def setup():
    try:
        with open('sleeps','r') as p:
            if raw_input('sleeps already exists. overwrite? [y/n]') == 'y':
                createpickle('sleeps')
    except:
        createpickle('sleeps')
        print "sleeps file created."
    try:
        with open('wakes','r') as p:
            if raw_input('wakes already exists. overwrite? [y/n]') == 'y':
                createpickle('wakes')
    except:
        createpickle('wakes')
        print "wakes file created."
    print "setup completed."

def createpickle(filename):
    """creates a file with a pickle of an empty list"""
    with open(filename,'w') as p:
            pickle.dump([],p)

def sleep():
    with open('sleeps','r+') as p:
        sleeps = pickle.load(p)
        sleeps.append(datetime.now())
        p.seek(0)
        pickle.dump(sleeps,p)
def wake():
    with open('wakes','r+') as p:
        wakes = pickle.load(p)
        wakes.append(datetime.now())
        p.seek(0)
        pickle.dump(wakes,p)

def unpickle(filename):
    with open(filename,'r') as p:
        file_contents = pickle.load(p)
    print str(file_contents)
