from django.db import models

# Create your models here.

class tbl_registrations(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=50)
    contact=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    status=models.CharField(max_length=10)
class tbl_login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=10)

# class Member(models.Model):
#     firstname=models.CharField(max_length=30)
#     lastname=models.CharField(max_length=30)
#     contact=models.CharField(max_length=30)
#     email=models.CharField(max_length=30)
#     password=models.CharField(max_length=12)


# def __str__ (self):
#     return self.firstname+""+self.lastname

# class mota:
#     db_table="web member"