from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
class Hobby(models.Model):
    title = models.CharField(max_length=50)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return self.title
class Book(models.Model):
    title = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    propic = models.ImageField(upload_to='profile_pics/', default='default_user.png', blank=True)

    def __str__(self):
        return self.name
    
    from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('LIB', 'Libros'),
        ('TEC', 'Tecnología'),
        ('OTR', 'Otros'),
    ]
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, by {self.user}"