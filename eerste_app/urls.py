from django.urls import path
from . import views
#url configuration
urlpatterns = [
path('login/', views.login_pagina),
]