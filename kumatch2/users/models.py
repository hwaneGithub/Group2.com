from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    nname = models.CharField(max_length=16, unique=True)
    is_staff = models.BooleanField('스태프 권한', default=False)


class Board(models.Model):
    b_title = models.CharField('제목', max_length=126)
    b_note = models.TextField('내용', null=False)
    b_writer = models.CharField('작성자', max_length=16)
    b_date = models.DateTimeField('작성일', auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.id, self.b_title)