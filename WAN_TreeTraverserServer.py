import sys
sys.path.append('./gen-py')

import time

from wandefinitions.ttypes import (MessageType, ResponseCode, Response)
from wantreetraverser.WANTreeTraverserService import Iface
from wantreetraverser.WANTreeTraverserService import Processor
import WAN_TreeTraverserClient
 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server.TNonblockingServer import TNonblockingServer

#threading is not proper for python
#TODO :: we need to check for TTForking server
#TSocket.py mentions in the comment that
#it doesn't cause GIL issues
from threading import Thread

import socket
 
class TreeTraverserHandler(Iface):
  def __init__(self):
    print("Server Handler initialized")

  def traverse(self, filename, attributes, data):
    print("Received request with details\n")
    print("Filename : " + filename)
    print("Metadata : " + str(attributes))
    print("Data : " + str(data))
    #this is a call to persist data locally
    self.persist(filename,attributes,data)
    time.sleep(15)
    #then pass on the message to other nodes
    self.visitChildren(filename, attributes, data)
    return Response(ResponseCode.SUCCESS, 'localhost', MessageType.PROPAGATE_STORE_DATA)

  def persist(self, filename, attributes, data):
    print("Persisting locally")
    pass

  def getChildren(self):
    #here return the actual children of the current node
    return [("localhost", 30000)]

  def visitChildren(self, filename, attributes, data):
    children = self.getChildren()
    childrenIps = [child[0] for child in children]
    #track childs that returned response , maybe check for ones
    # that are not returned and those which returned error message
    receivedResponse = []
    #threads = []
    for child in children:
      #pass
      thread = Thread(target=self.exploreChild, args=(child, filename, attributes, data))
     # threads += thread
      thread.start()

    #for t in threads:
     # t.join()
         
 
  def exploreChild(self,childNode, filename, attributes, data):
    clientIp = childNode[0]
    clientPort = childNode[1]
    client = WAN_TreeTraverserClient.WAN_TreeTraverserClient(clientIp, clientPort)
    client.send_request(filename, attributes, data)
    

handler = TreeTraverserHandler()
processor = Processor(handler)
transport = TSocket.TServerSocket(host='localhost', port=30000)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

#this will not fix the issue, blocking part is the code that will handle the
#incoming request and will block on that. Need some more clarity around this
#refer to : https://stackoverflow.com/questions/38533973/non-blocking-server-apache-thrift-python
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
#server = TNonblockingServer(processor, transport, tfactory, pfactory)
 
print("Starting server...")
server.serve()
print("Server started")
