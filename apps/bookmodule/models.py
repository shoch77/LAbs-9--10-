from django.db import models





class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50) 
    price = models.FloatField(default = 0.0) 
    edition = models.SmallIntegerField(default = 1)



#################################### Lab 9 


class Address(models.Model):
    city = models.CharField(max_length=100) 

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address)

    def __str__(self):
        return self.name


class Address2(models.Model):
    city = models.CharField(max_length=100) 

    def __str__(self):
        return self.city 

class Student2(models.Model):
    name = models.CharField(max_length=100)  
    age = models.IntegerField()  
    addresses = models.ManyToManyField(Address2, related_name="students")  # Many-to-Many Relationship

    def __str__(self):
        return self.name 
    
#################### Lab 10 Task 3

class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    
    def __str__(self):
        return self.title