from django.db import models

class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Картинка", upload_to="products/")
    article = models.CharField("Артикул", max_length=50, unique=True, default="N/A")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

        