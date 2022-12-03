from django.urls import path
from appweb.views import *

urlpatterns = [
    path("inicio/", inicio),
    path("perritos/", adoptar),
    path("perritos_resultado/", res_perro),
    path("gatitos/resultado/", res_gato),
    path("gatitos/", adoptar2),
    path("dar_adoptar/", daradop),
    path("reg_perros/", form_perros, name="formulario_de_perros"),
    path("reg_gatos/", form_gatos, name="formulario_de_gatos"),
    path("unite/", formapers, name="formulario_de_apersonas"),


]