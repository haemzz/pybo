from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)  # 글자 수 제한이 있는 데이터
    content = models.TextField()                # 글자 수 제한이 없는 데이터
    create_date = models.DateTimeField()        # 날짜, 시간 관련 속성
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)  # 글자 수 제한이 있는 데이터
    content = models.TextField()                                     # 글자 수 제한이 없는 데이터
    create_date = models.DateTimeField()                             # 날짜, 시간 관련 속성
    modify_date = models.DateTimeField(null=True, blank=True)