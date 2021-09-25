from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('create_user', views.register), # matches "create_user" action in index.html "register" is function name in views
]