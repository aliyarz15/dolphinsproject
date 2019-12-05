from django.db import models

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    price = models.IntegerField()
    content = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name