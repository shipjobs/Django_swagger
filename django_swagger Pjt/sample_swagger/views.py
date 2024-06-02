from django.shortcuts import render

# Create your views here.

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

#@swagger_auto_schema() 데코레이터를 활용하기위해 
from drf_yasg.utils import swagger_auto_schema

# "open_api_params.py" openapi schema를 view에 추가
from .open_api_params import get_params
from .open_api_params import post_params

#
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import ItemModel

# from .serializers import GetRequestSerializer
# from .serializers import GetResponseSerializer

# Create your views here.

# Viewset 장점
# queryset 사용으로 반복되는 CRUD 로직을 한번에 정의할 수 있음, ModelViewSet은 기본적으로 CRUD를 지원
# Router를 사용함으로써, URL설정을 다룰 필요가 없음
class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemModel.objects.all() #ItemModel의 모든 객체를 가져옴
    serializer_class = ItemSerializer
    
    
    
#APIView를 상속받으면, get, post, put, delete 함수를 통해 CRUD를 간편하게 사용 
class TestView(APIView):
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(manual_parameters=get_params)
    def get(self, request):
        return Response("TestView. Swagger 연동 테스트 입니다.")
    
    @swagger_auto_schema(request_body=post_params)
    def post(self, request):
        return Response("TestView. Swagger Schema 입니다.")
      
      
#manual_parameter 대신 query_serializer를 사용
# class TestView(APIView):
#     permission_classes = [permissions.AllowAny]
    
#     @swagger_auto_schema(query_serializer=GetRequestSerializer, responses={"200":GetResponseSerializer})
#     def get(self, request):
#         return Response("TestView. Swagger 연동 테스트 입니다.")
    
#     @swagger_auto_schema(manual_parameters=post_params)
#     def post(self, request):
#         return Response("TestView. Swagger Schema 입니다.")
      
      
#APIView를 상속받으면, get, post, put, delete 함수를 통해 CRUD를 간편하게 사용
#Serializer를 활용해 코드를 작성하면 가독성이 좋아 직관적으로 의미를 이해할 수 있고 openapi를 활용하는 것에 비해 코드 길이 자체도 줄어드는 장점
class SerializerView(APIView):
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema()
    def get(self, request):
        return Response("SerializerView. Swagger 연동 테스트")
    
    @swagger_auto_schema()
    def post(self, request):
        return Response("SerializerView. Swagger Schema")


