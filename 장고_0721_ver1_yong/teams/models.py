from django.db import models

# Create your models here.
class Team(models.Model):
	t_name = models.CharField(max_length=30)
	t_major = models.CharField(max_length=30)
	t_captain = models.CharField(max_length=30)
	t_memCount = models.IntegerField(default=0)

	def __str__(self):
		return self.t_name

		