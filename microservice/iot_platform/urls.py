from types import SimpleNamespace
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from iot_platform.views import *
from iot_platform.api.views import *

app_name='iot_platform'

urlpatterns = [
    path("", index, name="home"),
    path("login/", login, name="login"),
    path("dashboard/", dash, name="iotdash"),
    path("devices/", AllPayloadDevice, name="template2"),
    path("view-device/<str:device>/", NthPayloadDevice, name="nthdev"),
    path("add-device/", Client_add_device.as_view(), name="template2"),
    url('api/v2/', ApiPaylView.as_view(), name='payload'),
    url('api/dev_test/', APIPaylCheckView.as_view(), name='payloadx'),
]
urlpatterns = format_suffix_patterns(urlpatterns)