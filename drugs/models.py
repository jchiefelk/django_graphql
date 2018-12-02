from django.db import models

# Create your models here.
class Drugs(models.Model):
  name = models.CharField(max_length=50, null=True)
  in_chi = models.CharField(max_length=200, null=True)

  def __str__(self):
    return self.name
