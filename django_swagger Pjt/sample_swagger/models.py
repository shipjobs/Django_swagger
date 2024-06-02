from django.db import models


# Create your models here.
#models.py에서 모델 클래스를 설정하면 데이터베이스에 테이블이 생성
#Field Type 설명 참조: https://docs.djangoproject.com/en/3.2/ref/models/fields/
class ItemModel(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  cost = models.IntegerField()