from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home_doc'),
    path("doctors_view/",views.doctors_view,name="doctors_view"),
    path("doctor_loggedin/",views.doctor_loggedin,name="doctor_loggedin"),
    path("reset_tokens/<slug:doctor_id>/",views.reset_tokens,name="reset_tokens"),
    path("next_token/<slug:doctor_id>/<slug:current_token>/",views.next_token,name="next_token"),
    path("current_token/<slug:doctor_id>",views.current_token,name="current_token"),
    ]