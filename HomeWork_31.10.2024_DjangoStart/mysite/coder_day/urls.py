from django.urls import path

from . import views

urlpatterns = [
    path('', views.coder_day, name="coder_Day"),
]