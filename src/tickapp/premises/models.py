import datetime

from django.db import models
from django.utils import timezone

class Premise(models.Model):
  name = models.CharField(max_length=200)
  code = models.CharField(max_length=20)
  description = models.TextField(max_length=200, blank=True)
  pub_date = models.DateTimeField('published')
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  def __unicode__(self):
    return "%s -code: %s" % (self.name, self.code)

class Premise_Category(models.Model):
  premise = models.ForeignKey(Premise, on_delete=models.CASCADE)
  cat_name = models.CharField(max_length=200)
  cat_desc = models.TextField(max_length=100, blank=True)
  def __unicode__(self):
    return "%s" % (self.cat_name)

class Drink(models.Model):
  premise = models.ForeignKey(Premise_Category, on_delete=models.CASCADE)
  drink_name =  models.CharField(max_length=200)
  drink_price = models.IntegerField(default=0)
  drink_desc = models.TextField(max_length=100, blank=True)
  def __unicode__(self):
    return "%s" % (self.drink_name)

class Category(models.Model):
  cat_name = models.CharField(max_length=200)
  cat_desc = models.TextField(max_length=100, blank=True)