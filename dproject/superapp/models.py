from django.db import models

# Create your models here.
class Town(models.Model):
    name = models.CharField(max_length=50)
    # name = models.ForeignKey(Person, on_delete = models.CASCADE)

    def __str__(self):
        return (self.name)

class Person(models.Model):
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    objects = models.Manager()
    # hs = models.BooleanField()
    DoesNotExist = models.Manager

    def __str__(self):
        return (self.name)



class Company(models.Model):
    name = models.CharField(max_length=30)
    verbose_name = 'название компании'

    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    verbose_name = 'наименование продукции'

    def __str__(self):
        return self.name