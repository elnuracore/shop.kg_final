from django.db import models
from django.contrib.auth.models import User
from django.conf import settings # Добавьте импорт


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # ADD THIS LINE
    TYPE_PRODUCTS = (
        ("Meat", "Meat"),
        ("Bread", "Bread"),
        ("Drinkings", "Drinkings"),
        ("Oil", "Oil"),
        ("Chocolate", "Chocolate")
    )
    type_blog = models.CharField(max_length=150, choices=TYPE_PRODUCTS, default="Meat")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ... остальной код
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField('Review Text')
    rating = models.IntegerField('Rating', choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField('Date Created', auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.product}"
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
