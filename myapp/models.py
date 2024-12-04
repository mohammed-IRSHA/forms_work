from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name
class customer(models.Model):
    id=models.IntegerField(primary_key=True)
    item=models.CharField(max_length=20)
    rate=models.IntegerField()
    contact=models.ForeignKey(contact,on_delete=models.CASCADE,null=True)
    