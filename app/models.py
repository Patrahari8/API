from django.db import models

# Create your models here.
class EmpolyeeTable(models.Model):
    Ename=models.CharField(max_length=100)
    Esal=models.IntegerField()

    def __str__(self) -> str:
        return self.Ename
