from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Cart, CartItem, Order
from products.models import Product
from django.views.generic import CreateView
from .models import Order
from .forms import OrderForm

class CheckoutView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/checkout.html'
    success_url = '/' # Или на страницу "Спасибо за заказ"

    def form_valid(self, form):
        # Дополнительная логика (привязка пользователя к заказу)
        form.instance.user = self.request.user
        return super().form_valid(form)

# Представление для отображения корзины
class CartView(LoginRequiredMixin, ListView):
    template_name = 'basket/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        # Получаем или создаем корзину для текущего пользователя
        cart, _ = Cart.objects.get_or_create(user=self.request.user, is_active=True)
        return cart

# Класс для добавления товара (заменяет функцию add_to_cart)
class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user, is_active=True)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()
        messages.success(request, f'{product.product_name} добавлен в корзину!')
        return redirect('basket:cart_view')

# Класс для обновления количества (заменяет функцию update_cart_item)
class UpdateCartItemView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('basket:cart_view')

# Класс для удаления (заменяет функцию remove_from_cart)
class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
        messages.success(request, 'Товар удален из корзины!')
        return redirect('basket:cart_view')