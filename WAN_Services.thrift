namespace py waniotservices

typedef i64 int

service WideAreaNetworkIoTService{
	int put(1:string filename,2:map<string,string> attributes,3:binary data)
	int get(1:int  id)
	int find(1:string filename)
	int replicate(1:string filename)

}