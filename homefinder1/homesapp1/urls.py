from django.contrib import  admin
from django.urls import  path
from django.conf.urls import include,url
from .import views

urlpatterns =[
    url(r'^$',views.IndexView.as_view(),name='Index'),
    #/homesapp1/1
    url(r'^(?P<pk>[0-9]+)/$',views.LocationView.as_view(),name='property'),

    # /homesapp1/1/2
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/$',views.PropertyDetails.as_view(),name='propertyview'),
]