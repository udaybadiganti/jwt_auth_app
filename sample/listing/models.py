from django.db import models
from django.utils.timezone import now

# Create your models here.

class Listing(models.Model):
	category = models.CharField(max_length = 255)
	item_name = models.CharField(max_length = 255)
	slug = models.SlugField(unique = True)
	created_date = models.DateTimeField(default = now)

	def __str__(self):
		return self.item_name
