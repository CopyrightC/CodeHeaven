from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    feedback = models.CharField(max_length=700)
    date = models.DateField()
    def __str__(self):
        return self.name
    