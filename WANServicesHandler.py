#!/usr/bin/env python

import sys
sys.path.append('./gen-py')

from waniotservices.WideAreaNetworkIoTService import *
from waniotservices.ttypes import *

class WANServicesHandler:
    def __init__(self):
        self.log = {}

    #Put is called by a client to put his data in the storage system
    #put does 2 things, 1 store locally 2. propagate ahead (with/without storage)
    def put(self,filename,attributeMap,binaryData):

        print("The filename is ",filename)

        return 1

    #Get is called by a client with the filename is argument to retreive the data
    def get(self,filename):

        print("The filename trying to get ",filename)

        return 1

    #Find is to search for the given filename
    def find(self,filename):

        print("The filename trying to search is ", filename)

        return 1

    #Replicate will percolate data in the node tree
    def replicate(self,filename):

        print("The filename that is trying to percolate is",filename)

        return 1

print("WAN Service Handler ")

