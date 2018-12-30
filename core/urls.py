from django.urls import path
from core.views import *

urlpatterns = [
 path("mail/", mail),
 path("", home)
]
