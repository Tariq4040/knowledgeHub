from django.db import models

# Create your models here.
class Contact1(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    zip=models.CharField(max_length=10)
    disc=models.CharField(max_length=200)
    date=models.DateField()

    def __str__(self):
        return self.name
    
class Personal_Contact_Form(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=20)
    
#     country=models.CharField(max_length=30)
#     state=models.CharField(max_length=30)
# Personal_Contact_Form.save(country, state)

    def __str__(self):
        return self.name
    
   