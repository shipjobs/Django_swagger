from datetime import date
import string
from rest_framework import serializers

from .models import ItemModel

#serialiezer란 장고 모델 데이터를 json타입으로 바꿔주는 작업 을 수행하는 Serializer.py 파일
# 설정한 models.py의 Item class를 import한다.
# 설치한 rest_framework에서 serializers를 import한다.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')    
        
        
# request ={
#   'param1': serializers.IntegerField(),
#   'param2': string,
#   'param3': date,
# }

# response ={
#   'status': 200,
#   'message': 'SUCCESS'
# }

reques ={
    "school_name": "KNU",
    "student_list": [
        {
            "first_name": "Hanseul",
            "last_name": "Jo"
        },
        {
            "first_name": "Hanseul",
            "last_name": "Cho"
        }
    ]
}

response = {
    "status": 201,
    "message": "SUCCESS"
}

########
# v1
# - serializer
# - test 
#######
# v1/seializer/ getrequest  
class GetRequestSerializer(serializers.Serializer):
    param1 = serializers.IntegerField()
    param2 = serializers.CharField(max_length=20)
    param3 = serializers.DateField()
  # v1/seializer/ getresponse

# v1/seializer/ getresponse
class GetResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()

# v1/test/ postrequest
class PostRequestSerializer(serializers.Serializer):
    school_name = serializers.CharField()
    student_list = serializers.ListField()

# v1/test/ postresponse
class PostResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
  
    
