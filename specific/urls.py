from django.urls import path
from specific.views import *

app_name='anything'
urlpatterns=[
    path('swethabhai/',swethabhai,name='swethabhai'),
]
