from.views import call,Admin_Registeration
from django.conf.urls import url
from.views import Admin_Registeration,Admin_RegisterationCRD

urlpatterns=[
    url(r"^get_call_1/(?P<id>\d+)/$",Admin_Registeration.as_view()),
    url(r"^serializers/$",Admin_RegisterationCRD.as_view()),
]