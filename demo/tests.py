from django.test import TestCase
from spyne.server.null import NullServer
from spyne.application import Application
from .views import SoapService
# Create your tests here.

soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

null = NullServer(soap_app, ostr=True)
ret_stream = null.service.hello('RED')
ret_string = ''.join(ret_stream)
print(ret_string)