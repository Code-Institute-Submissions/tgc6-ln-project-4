from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Product(models.Model):
    name = models.CharField(blank=False, max_length=80)
    selling_price = models.DecimalField(blank=False,
                                        max_digits=4,
                                        decimal_places=2)
    quantity = models.IntegerField(blank=False)
    cover = CloudinaryField()

    def __str__(self):
        return self.name
