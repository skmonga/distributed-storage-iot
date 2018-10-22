namespace py wandefinitions

enum MessageType {
  PROPAGATE_DATA = 1,
  PROPAGATE_STORE_DATA = 2,
  STORE_DATA = 3
}

enum ResponseCode {
  SUCCESS = 0,
  ERROR = 1
}

struct Response {
  //need to check for byte as single byte can do
  1: required ResponseCode responseCode = ResponseCode.ERROR,
  //this is used in case failure occurs so that server can retry for the failing receiver
  2: required string receiverIdentity,
  //assuming PROPAGATE_STORE_DATA is our default
  3: optional MessageType msgType = 2
}
