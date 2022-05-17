from django.db import models

# Create your models here.

class Catigory(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name
  
class Book(models.Model):
  status_book = [
    ('available', 'available'),
    ('rental', 'rental'),
    ('solid', 'solid'),
  ]
  
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100, null=True, blank=True)
  photo_book = models.ImageField(null=True, blank=True)
  photo_author = models.ImageField(null=True, blank=True)
  pages = models.IntegerField(null=True, blank=True)
  price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  retal_period = models.IntegerField(null=True, blank=True)
  total_rental = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  active = models.BooleanField(default=True)
  status = models.CharField(max_length=50, choices=status_book)
  catigory = models.ForeignKey(Catigory, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
  
  @property
  def imageUrl(self):
    try:
      photobook = self.photo_book.url
    except:
      photobook = ''
    try:
      photoauthor = self.photo_author.url
    except:
      photoauthor = ''
    return photobook or photoauthor