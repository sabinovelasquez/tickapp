import datetime

from django.db import models
from django.utils import timezone

class Premise(models.Model):
  name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('published')
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Premise, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)