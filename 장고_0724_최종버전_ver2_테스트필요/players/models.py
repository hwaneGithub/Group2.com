from django.db import models


# Create your models here.
class Player(models.Model):
    p_club = models.CharField(max_length=30)
    p_name = models.CharField(max_length=10)
    p_gender = models.CharField(max_length=5)
    p_nname = models.CharField(max_length=16)

    def __str__(self):
        return '[{}] {}'.format(self.p_club, self.p_name)
