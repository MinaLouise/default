from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length = 24)
    phone_number = models.CharField(max_length = 10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    # pfp = models.ImageField()


=======
    profile_picture = models.ImageField(null=True, blank=True)
    
>>>>>>> 11bf467e31904cc61940b0b21c761655a7efdccb

class Properties(models.Model):
    user_props = models.ForeignKey(Account, on_delete=models.CASCADE)
    price = models.IntegerField()
    address = models.TextField()
    city = models.TextField()
    zip_code = models.IntegerField()
    size = models.IntegerField()
    available = models.BooleanField()
    # photo = models.ImageField()

