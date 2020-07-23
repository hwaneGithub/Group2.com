from django.db import models


# Create your models here.
class Match(models.Model):
    m_date = models.CharField(max_length=10)
    m_time = models.CharField(max_length=10)
    m_place = models.CharField(max_length=60)
    m_nname = models.CharField(max_length=30)
    m_gender = models.CharField(max_length=10)
    m_num = models.CharField(max_length=5)
    m_rival = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return '[{}] {}'.format(self.m_date, self.m_nname)

