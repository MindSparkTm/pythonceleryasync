from suds.client import Client
from suds.cache import NoCache

my_client = Client('http://127.0.0.1:8000/demo/soap_service/?WSDL',cache=NoCache())
my_client.set_options(headers={'username': 'we','password':'kkdkd'})

print ('Function color exists: ', my_client.service.exists('BLUE'))
print ('Function validateandadd: ', my_client.service.validateandadd('GREEN'))


