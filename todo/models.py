from django.db import models

# Create your models here.
class Item(models.Model):
    Item_name = models.CharField(max_length=30)
    add_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Item_name

