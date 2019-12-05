from django.db import models


class Cart(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    price = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name