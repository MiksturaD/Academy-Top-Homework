from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('news', views.news, name='news'),
    path('governance', views.governance, name="governance"),
    path('facts', views.facts, name="facts"),
    path('contact', views.contact, name="contact"),

]