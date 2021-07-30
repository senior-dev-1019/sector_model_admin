from django.db import models

# Create your models here.

class Sector(models.Model):
	sector_name = models.CharField(max_length=64)

	def _str_(self):
		return f"{self.sector_name}"

class Organization(models.Model):
	org_sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='org_sector')
	org_name = models.CharField(max_length=64)
	legal_name = models.CharField(max_length=64)
	alt_name1 = models.CharField(max_length=64)
	alt_name2 = models.CharField(max_length=64)
	alt_name3 = models.CharField(max_length=64)
	Ticker = models.CharField(max_length=10)

	def _str_(self):
		return f"{self.org_name}"