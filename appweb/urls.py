from django.urls import path
from appweb.views import *

urlpatterns = [
    path("inicio/", inicio),
    path("adopta/", adoptar),


]