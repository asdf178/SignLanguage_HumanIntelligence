from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Action(models.Model): # 유저마다 학습한 action을 저장함
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="action", null=True) # action을 학습한 유저의 정보
    name = models.CharField(max_length=200) # action의 이름
    complete = models.BooleanField(default=False) # action의 학습을 완료했는지 여부

    def __str__(self):
        return self.name