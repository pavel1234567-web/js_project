from django.contrib import admin
from django.utils.html import mark_safe
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("article","name", "price","image_preview")
    search_fields = ("article","name","price",)
    readonly_fields = ("image_preview",)  # превью в форме редактирования (не редактируемое)


    def image_preview(self, obj):
            if obj.image:
                return mark_safe(
                f'<a href="{obj.image.url}" target="_blank">'
                f'<img src="{obj.image.url}" style="height:100px;width:250px; object-fit:contain;" />'
                '</a>'
            )
            return "Нет изображения"
        
    image_preview.short_description = "Превью"