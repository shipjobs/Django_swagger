#sample_swagger/urls.py 을 생성함

from django.urls import path
#from rest_framework.routers import DefaultRouter
from sample_swagger.views import TestView
from sample_swagger.views import SerializerView

# Create a router and register our viewsets with it.
# router = DefaultRouter()

# The API URLs are now determined automatically by the router.
urlpatterns = [ 
            path('v1/test/', TestView.as_view(), name='test'),
            path('v1/serializer/', SerializerView.as_view(), name='serializer'),
        ]