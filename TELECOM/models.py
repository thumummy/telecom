from django.db import models



# Create your models here.

class customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname+" "+self.lastname


class ourservices(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    providercontact = models.IntegerField(default=12)


    def __str__(self):
        return self.name

class imagemodel(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length= 50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class workers(models.Model):
    fullname = models.CharField(max_length=50)
    ID = models.IntegerField(primary_key='true')
    contact = models.IntegerField(default=12)
    position = models.CharField(max_length=30)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname