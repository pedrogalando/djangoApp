from django.db import models

# Create your models here. 
class Framework(models.Model):  
    nombre = models.CharField(max_length=100)  
    autor = models.CharField(max_length=100)   
    descripcion = models.CharField(max_length=100)  

    class Meta:  
        db_table = 'framework'
