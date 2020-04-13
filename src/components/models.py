from django.db import models

# Create your models here.

class Specification(models.Model):
    SpecName = models.CharField(max_length=50, blank=True)
    SpecValue = models.CharField(max_length=50, blank=True)

class Component(models.Model):
    CompName = models.CharField(max_length=100)
    Company = models.CharField(max_length=100, default="None")
    Description = models.TextField(blank=True, null=True)
    State = models.CharField(max_length=50, blank=False, default="INA")
    NextState = models.CharField(max_length=50, blank=False, default="Make")
    AvgPrice = models.DecimalField(max_digits=20, decimal_places=2)
    Spec = models.ForeignKey(Specification, on_delete=models.CASCADE,)



