from .views import *
from django.conf.urls import url
from .allcompany import *


urlpatterns = [
    url(r"xiamen$", xiamen,),
    url(r"allsearch$", allsearch, )
]