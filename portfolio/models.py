from django.db import models
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    slug = models.SlugField("URL", max_length=100, unique=True, blank=True)

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,  # Если категорию удалят, товар останется
        null=True,
        blank=True,
        related_name="products",
    )
    name = models.CharField("Название", max_length=200)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Картинка", upload_to="products/")
    article = models.CharField("Артикул", max_length=50, unique=True, default="N/A")
    description = models.TextField("Описание", blank=True)
    slug = models.SlugField("URL", max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
