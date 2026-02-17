from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.management import call_command
from .models import Product

@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def auto_export(sender, **kwargs):
    call_command("export_products")
