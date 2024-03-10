from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return str(self.username)


class user(models.Model):
    id = models.AutoField (primary_key=True)
    name = models.CharField(max_length=100,blank=False)


    class Meta:
        db_table = "user_table"

gender_choices={
    ('Male','Male'),('Female','Female'),('Prefer not to say','Prefer not to say')
}
class register(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password= models.CharField(max_length=100, blank=False, unique=False)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Others", "Others"))
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    pho = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table="register_table"
    def _str_(self):
        return str(self.username)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def _str_(self):
        return self.email


class Feedback(models.Model):
    customer_name = models.CharField(max_length=30)
    email = models.EmailField()
    feedback = models.TextField()
    date = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.customer_name
    
