from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('search/', views.ProductListView.as_view(), name='search'),
    path('product/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('review/delete/<int:review_id>/', views.ReviewDeleteView.as_view(), name='delete_review'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
