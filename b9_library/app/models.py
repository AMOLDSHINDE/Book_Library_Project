from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        db_table = "book"   # ha book new table create kartoy ani db madhe already book ahe tyamule navin create hot nahi
    def __str__(self):
        return self.name
    