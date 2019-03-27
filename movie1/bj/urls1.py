from django.urls import path, include
#from django.conf.urls import url
from bj.views.login_view import *

urlpatterns = [
    path('register/',regist),
    path('login/',login)
]