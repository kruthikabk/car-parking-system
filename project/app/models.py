from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    desc=models.TextField(max_length=300)

    def _str_(self):
        return self.name


class BlogPost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    name=models.CharField(max_length=25)
    timeStamp = models.DateTimeField(blank=True)

    def __int__(self):
        return self.sno