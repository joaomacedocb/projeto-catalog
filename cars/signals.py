from django.db.models.signals import post_save, post_delete, pre_save
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

@receiver(pre_save, sender=Car)
def item_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Sem descrição cadastrada.'

@receiver(post_save, sender=Car)
def item_post_save(sender, instance, **kwargs):
    item_inventory_update()

@receiver(post_delete, sender=Car)
def item_post_delete(sender, instance, **kwargs):
    item_inventory_update()