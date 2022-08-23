from django.db import models

# Create your models here.


class Application(models.Model):
    groom = models.BooleanField(default=False)
    cat = models.BooleanField(default=False)
    walk = models.BooleanField(default=False)
    overnight = models.BooleanField(default=False)
    visit = models.BooleanField(default=False)
    jewelry = models.BooleanField(default=False)
    yard_cleaning = models.BooleanField(default=False)
    house_cleaning = models.BooleanField(default=False)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=30)
    pet_name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    vet_name = models.CharField(max_length=30)
    accepted = models.BooleanField(default=False)


    def __str__(self):
        return self.fname + " " +self.lname
