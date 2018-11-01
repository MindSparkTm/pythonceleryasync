from suds.client import Client
from suds.cache import NoCache

my_client = Client('http://127.0.0.1:8000/demo/soap_service/?WSDL',cache=NoCache())
# username ='raaj'
# password ='mom12345'
# my_client.set_options(headers=(username , password))
print ('Function hello: ', my_client.service.exists('jdkdkdkdk'))
print ('Function hello: ', my_client.service.validateandadd('jdjjjdjdjd'))


