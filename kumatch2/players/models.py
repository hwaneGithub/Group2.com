from django.db import models

# Create your models here.
class Player(models.Model):
	p_pid = models.CharField(max_length=30)
	p_nick = models.CharField(max_length=50)
	p_email = models.CharField(max_length=30)
	p_name = models.CharField(max_length=30)
	p_birth =  models.CharField(max_length=10)
	p_position = models.CharField(max_length=30)
	p_team = models.CharField(max_length=30)

	def __str__(self):
		return self.p_name