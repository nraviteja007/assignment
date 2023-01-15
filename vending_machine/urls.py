from django.urls import path
from . import views
urlpatterns = [
    path("",views.departments,name="departments"),
    path("doctors/",views.doctors,name="doctors"),
    path("doctors/token/",views.token,name="token"),
    path("doctors/token/token-generation/",views.token_generation,name="token_generation"),
]