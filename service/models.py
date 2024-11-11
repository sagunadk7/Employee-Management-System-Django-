from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=65)
    address = models.TextField()
    phone = models.IntegerField()
    
    
    def __str__(self):
        return self.name
      
    

# Create your models here.