import sys
sys.path.append('./gen-py')

arguments = sys.argv[1:]
portNum = int(arguments[0])
 
from wantreetraverser.WANTreeTraverserService import Client
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class WAN_TreeTraverserClient(object):
  def __init__(self, ipAddr, portNum):
    self.ip = ipAddr
    self.port = portNum

  def send_request(self, filename, attributes, data):  
    try:
      transport = TSocket.TSocket(self.ip, self.port)
      #use buffered sockets, raw sockets slow
      transport = TTransport.TBufferedTransport(transport)
      protocol = TBinaryProtocol.TBinaryProtocol(transport)
      client = Client(protocol)
      transport.open()
      #start the exchange here
      client.traverse(filename, attributes, data)
      transport.close()
    except Thrift.TException as tx:
      print(tx.message)

if __name__ == '__main__':
  client = WAN_TreeTraverserClient('localhost', portNum)
  client.send_request('a.txt', {}, bytearray(b'\x00\x0F'))


