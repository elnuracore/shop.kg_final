from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название бренда")

    def __str__(self):
        return self.name

class ClothesModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название одежды")
    image = models.ImageField(upload_to='clothes/', verbose_name="Фото")
    # ManyToMany по условию
    brands_name = models.ManyToManyField(Brand, verbose_name="Бренды")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title