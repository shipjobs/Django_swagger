from datetime import date
import string
# from rest_framework import serializers

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

# class GetRequestSerializer(serializers.Serializer):
#     param1 = serializers.IntegerField()
#     param2 = serializers.CharField(max_length=20)
#     param3 = serializers.DateField()
    
# class GetResponseSerializer(serializers.Serializer):
#     status = serializers.CharField()
#     message = serializers.CharField()
    
# class PostRequestSerializer(serializers.Serializer):
#     school_name = serializers.CharField()
#     student_list = serializers.ListField()

# class PostResponseSerializer(serializers.Serializer):
#     status = serializers.CharField()
#     message = serializers.CharField()