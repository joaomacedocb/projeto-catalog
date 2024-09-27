from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver

from cars.models import Car, ItemInventory

def item_inventory_update():
    items_count = Car.objects.all().count()
    items_value = Car.objects.all().aggregate(
        total_value = Sum('value')
    )['total_value']
    ItemInventory.objects.create(
        items_count = items_count,
        items_value = items_value
    )


@receiver(post_save, sender=Car)
def item_post_save(sender, instance, **kwargs):
    item_inventory_update()

@receiver(post_delete, sender=Car)
def item_post_delete(sender, instance, **kwargs):
    item_inventory_update()