from django.conf.urls import url
from dlapp import views

urlpatterns=[
    url('',views.index,name='index'),
]
