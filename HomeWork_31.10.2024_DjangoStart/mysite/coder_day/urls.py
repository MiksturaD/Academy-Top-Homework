from django.urls import path

from . import views

urlpatterns = [
    path('', views.b_day, name="coder_Day"),
]