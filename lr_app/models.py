from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    status = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        db_table = 't_user'