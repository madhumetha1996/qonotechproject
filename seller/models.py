from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    # Add other fields as per your requirements

    def __str__(self):
        return self.name
