from django.db import models

# Create your models here.
class users (models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    class Meta:
        db_table="users"
        
        
        #creation_date = models.DateTimeField(default=timezone.now)
