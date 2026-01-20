import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from products.models import Product

products = [
    {
        'product_name': 'Fresh Beef',
        'description': 'High quality fresh beef from local farms',
        'price': 1200.00,
        'type_blog': 'Meat',
    },
    {
        'product_name': 'Whole Wheat Bread',
        'description': 'Healthy bread baked fresh daily',
        'price': 80.00,
        'type_blog': 'Bread',
    },
    {
        'product_name': 'Orange Juice',
        'description': '100% pure orange juice with no additives',
        'price': 250.00,
        'type_blog': 'Drinkings',
    },
    {
        'product_name': 'Olive Oil',
        'description': 'Extra virgin olive oil, imported from Italy',
        'price': 1500.00,
        'type_blog': 'Oil',
    },
    {
        'product_name': 'Dark Chocolate',
        'description': '70% cocoa dark chocolate bar',
        'price': 350.00,
        'type_blog': 'Chocolate',
    },
    {
        'product_name': 'Chicken Breast',
        'description': 'Boneless chicken breast, skinless',
        'price': 800.00,
        'type_blog': 'Meat',
    },
    {
        'product_name': 'White Bread',
        'description': 'Soft white bread loaf',
        'price': 60.00,
        'type_blog': 'Bread',
    },
    {
        'product_name': 'Apple Juice',
        'description': 'Fresh pressed apple juice',
        'price': 200.00,
        'type_blog': 'Drinkings',
    },
]

for product_data in products:
    product, created = Product.objects.get_or_create(
        product_name=product_data['product_name'],
        defaults=product_data
    )
    if created:
        print(f"✅ Created: {product.product_name} - {product.price} KGS")
    else:
        print(f"ℹ️  Already exists: {product.product_name}")

print(f"\n🎉 Total products in database: {Product.objects.count()}")
