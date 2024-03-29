import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Poll(models.Model):
	
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question

	def was_recently_published(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now
	was_recently_published.admin_order_field = 'pub_date'
	was_recently_published.short_description = 'Published Recently'

class Choice(models.Model):
	
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text

