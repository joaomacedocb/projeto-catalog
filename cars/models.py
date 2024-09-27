from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    plate = models.CharField(max_length=7, blank=True, null=True)
    factoryYear = models.IntegerField(blank=True, null=True)
    modelYear = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
    
class ItemInventory(models.Model):
    id = models.AutoField(primary_key=True)
    items_count = models.IntegerField()
    items_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.items_count} - {self.items_value}'
