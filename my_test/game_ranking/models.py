from django.db import models

# Create your models here.


class UserInfo(models.Model):
    client_id = models.CharField(max_length=50)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.client_id