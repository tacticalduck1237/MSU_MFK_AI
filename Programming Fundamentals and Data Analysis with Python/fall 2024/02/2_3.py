uri=input()
protocol_end=uri.find("://")+3
domain_end=uri.find("/", protocol_end)
if domain_end==-1:
    domain_end=len(uri)
print(uri[protocol_end:domain_end])
