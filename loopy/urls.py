from django.urls import path
from . import views

app_name = "loopy"
urlpatterns = [
    path("", views.index, name="index")
]