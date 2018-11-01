from django.db import models

# Create your models here.
class Color(models.Model):
    id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=300)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.id) + " : " + self.color_name

class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.CharField(max_length=300)
    response = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.id) + " : " + self.request+":"+self.response




