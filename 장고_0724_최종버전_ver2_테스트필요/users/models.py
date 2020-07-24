from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    nname = models.CharField(max_length=16, unique=True)
    passwordck = models.CharField(max_length=16)
    stu_num = models.CharField(max_length=16)
    gender = models.CharField(max_length=16)
    favorite = models.CharField(max_length=16)
    birth_year = models.CharField(max_length=16)
    birth_month = models.CharField(max_length=16)
    birth_day = models.CharField(max_length=16)
    is_staff = models.BooleanField('스태프 권한', default=False)


class Notice(models.Model):
    n_title = models.CharField(max_length=30)
    n_memo = models.TextField(null=False)
    n_writer = models.CharField(max_length=20)
    n_date = models.DateTimeField('작성일', auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.id, self.n_title)


''' 전에쓰던거 참고하려고 남겨둡니다^^
class Board(models.Model):
    b_title = models.CharField('제목', max_length=126)
    b_note = models.TextField('내용', null=False)
    b_writer = models.CharField('작성자', max_length=16)
    b_date = models.DateTimeField('작성일', auto_now_add=True)
    b_id = models.ForeignKey('users.User', related_name='boards', on_delete=models.CASCADE) #b_id_id 필드로 변경됨
    # (실제 데이터베이스에 b_id_id 로 필드명이 변경된 이유는 ForeignKey 필드의 또다른 속성인
    # to_field 값을 설정하지 않아 기본값인 참조하는 모델의 pk 필드인 id로 설정이 된 것)

    def __str__(self):
        return '[{}] {}'.format(self.id, self.b_title)
'''
