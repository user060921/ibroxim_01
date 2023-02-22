from django.db import models
import datetime
from django.contrib.auth.models import User

class vazifa(models.Model):
    gender_type=(
        ('namunali','namunali'),('yaxshi','yaxshi'),('qoniqasiz','qoniqasiz')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    narxi = models.FloatField(max_length=250)
    sifati = models.CharField(max_length=50,choices=gender_type)
    qushilgansana=models.DateField(null=True,default=datetime.datetime.now())
    def __str__(self):
        return f"{self.user} - {self.title} - {self.qushilgansana}"