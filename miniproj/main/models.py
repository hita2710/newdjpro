from django.db import models

# Create your models here.
class UserDetails(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mailid = models.EmailField(max_length=254)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    confpassword = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}'

class FileDetails(models.Model):
    username = models.CharField(max_length=10)
    filename=models.CharField(max_length=20,default='filename')
    fileupl = models.FileField(upload_to='files/')

    def __str__(self):
        return f'{self.username} {self.filename}'
