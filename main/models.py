from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
	"""Category class which owns skill"""

	title = models.CharField('категория',max_length=100)
	icon = models.ImageField('иконка', null=True, blank=True)

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "категория"
		verbose_name_plural = "категории"


class Order(models.Model):
	name = models.CharField('имя заказчика',max_length=100)
	telephone = models.CharField('номер телефона',max_length=100)
	#category = models.ForeignKey(Category, verbose_name='категория')
	date_of_order = models.CharField('дата и время исполнения заказа',max_length=200, default="не указан")
	address = models.CharField('адрес',max_length=400, default="не указан")
	value = models.CharField('помещение',max_length=400, default="не указан")
	date_of_submition = models.DateTimeField('дата и время поступления заявки', default=datetime.now)
	def __unicode__(self):
		return self.name + " " + self.telephone

	class Meta:
		verbose_name = "заявка"
		verbose_name_plural = "заявки"
		


class Mail(models.Model):
	name = models.CharField('имя отправителя',max_length=100)
	email = models.CharField(max_length=100)
	title = models.CharField('тема',max_length=100)
	body = models.CharField('сообщение',max_length=1000)
	date = models.DateTimeField('дата отправления', default=datetime.now)
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "сообщение"
		verbose_name_plural = "сообщения"