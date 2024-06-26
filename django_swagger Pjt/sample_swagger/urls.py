#sample_swagger/urls.py 을 생성함

from django.urls import include, path
#from rest_framework.routers import DefaultRouter
from sample_swagger.views import TestView
from sample_swagger.views import SerializerView

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views #views.py import

# Create a router and register our viewsets with it.
router = routers.DefaultRouter() #DefaultRouter를 설정
router.register('ItemModel_ItemViewSet', views.ItemViewSet) #itemviewset 과 itemModel 이라는 router 등록

 

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API. (    )
urlpatterns = [ 
            path('', include(router.urls)),

            path('v1/test/', TestView.as_view(), name='test'),
            path('v1/serializer/', SerializerView.as_view(), name='serializer'),
        ]