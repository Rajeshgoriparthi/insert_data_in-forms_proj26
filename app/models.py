from django.db import models

# Create your models here.

class department(models.Model):
    did=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=30)
    loc=models.CharField(max_length=30)

    def __str__(self):
        return self.dname


class employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    job=models.CharField(max_length=30)
    sal=models.IntegerField()
    did=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename