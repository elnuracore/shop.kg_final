import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from products.models import Product

# Create sample products if they don't exist
products_data = [
    {
        'product_name': 'Fresh Beef',
        'description': 'High quality fresh beef',
        'price': 500,
        'type_blog': 'Meat',
    },
    {
        'product_name': 'Whole Wheat Bread',
        'description': 'Healthy whole wheat bread',
        'price': 80,
        'type_blog': 'Bread',
    },
    {
        'product_name': 'Orange Juice',
        'description': 'Fresh orange juice',
        'price': 150,
        'type_blog': 'Drinkings',
    },
    {
        'product_name': 'Olive Oil',
        'description': 'Extra virgin olive oil',
        'price': 800,
        'type_blog': 'Oil',
    },
    {
        'product_name': 'Dark Chocolate',
        'description': '70% dark chocolate',
        'price': 250,
        'type_blog': 'Chocolate',
    },
]

for product_data in products_data:
    product, created = Product.objects.get_or_create(
        product_name=product_data['product_name'],
        defaults=product_data
    )
    if created:
        print(f"Created product: {product.product_name}")
    else:
        print(f"Product already exists: {product.product_name}")

print("Sample products created successfully!")
