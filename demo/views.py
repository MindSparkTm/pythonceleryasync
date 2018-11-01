from .models import Color
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from spyne.model.complex import ComplexModel
from spyne.model.primitive import Unicode
from .tasks import generate_logs


# Create your views here.

class Requestheader(ComplexModel):
    username = Unicode
    password = Unicode


class SoapService(ServiceBase):
    __tns__ = 'spyne.examples.authentication'
    __in_header__ = Requestheader

    # to check if a color exists
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def exists(ctx, name):
        username = ctx.in_header.username
        password = ctx.in_header.password
        print('username', username, password)

        colors = {'RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'VIOLET'}

        if name in colors:

            if Color.objects.filter(color_name=name).exists():
                generate_logs.delay(request=name, response=True)

                return True
            else:
                generate_logs.delay(request=name, response=True)
                return False



        else:
            generate_logs.delay(request=name, response=False)

            return False

    # to validate the color name and add it to database if doesnt exists
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def validateandadd(ctx, name):

        # username = ctx.in_header.username
        # password = ctx.in_header.password
        # print('username', username, password)

        colors = {'RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'VIOLET'}

        if name in colors:

            colorobj, created = Color.objects.get_or_create(color_name=name)

            if created:
                generate_logs.delay(request=name, response=True)

                return True
            else:
                generate_logs.delay(request=name, response=False)

                return False

        else:
            generate_logs.delay(request=name, response=False)

            return False


soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)
