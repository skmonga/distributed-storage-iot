include "WAN_Definition.thrift"

namespace py wantreetraverser

service WANTreeTraverserService{
  WAN_Definition.Response traverse(1:string filename,2:map<string,string> attributes,3:binary data)
}
