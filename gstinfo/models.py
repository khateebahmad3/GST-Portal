from django.db import models

class Registration(models.Model):
	trn = models.CharField(max_length=50)
	name = models.CharField(max_length=150)
	email = models.EmailField(default='')
	epassword = models.CharField(max_length=128, default='')
	phone_number = models.CharField(max_length=10, default=0)
	status = models.CharField(max_length=20)
	gstin = models.CharField(max_length=50, default='', blank=True)
	username = models.CharField(max_length=150, default='', blank=True)
	upassword = models.CharField(max_length=128, default='', blank=True)

	def __str__(self):
		return self.trn

class ReturnInfo(models.Model):
	name = models.CharField(max_length=150)
	username = models.CharField(max_length=150)
	upassword = models.CharField(max_length=128)
	phone_number = models.CharField(max_length=10)
	email = models.EmailField(default='')
	epassword = models.CharField(max_length=128, default='')
	month = models.CharField(max_length=12, default='')
	status = models.CharField(max_length=11, default="Not Filed")

	def __str__(self):
		return self.username