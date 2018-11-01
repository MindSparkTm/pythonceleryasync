from . import views
from django.conf.urls import url, include

urlpatterns = (


)

urlpatterns += (
    # urls for models

    url(r'^soap_service/', views.my_soap_application),

)
