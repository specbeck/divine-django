from django.urls import path
from . import views

appname = "default"
urlpatterns = [
    path("", views.index, name="index")
]