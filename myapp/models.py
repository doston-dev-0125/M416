from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.username


DIFF_CHOICES =(
    ('pc', 'pc'),
    ('gpc','gpc'),
    ('vr','vr'),
    ('xbox','xbox'),
    ('ps','ps')
    )
class Book(models.Model):
    game=models.CharField(max_length=5, choices=DIFF_CHOICES, default='ps')
    date=models.DateField()
    time=models.TimeField()
    number=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.game
    
    