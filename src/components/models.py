from django.db import models

# Create your models here.

class Component(models.Model):
    CompName = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)
    State = models.CharField(max_length=50, blank=False)
    NextState = models.CharField(max_length=50, blank=False)


class Specification(models.Model):
    SpecName = models.CharField(max_length=50)
    SpecValue = models.CharField(max_length=50)

