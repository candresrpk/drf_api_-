from django.db import models

# Create your models here.
class Programmer(models.Model):
    fullname = models.CharField(
        max_length=250,
    )
    nickname = models.CharField(
        max_length=100
    )
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.fullname} or {self.nickname}"