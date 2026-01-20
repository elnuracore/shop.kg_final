from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Product, Review
from .forms import ReviewForm

class ProductListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('s')
        if query:
            return Product.objects.filter(product_name__icontains=query)
        return Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all().order_by('-created_at')
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = self.object
            review.user = request.user
            review.save()
            messages.success(request, 'Комментарий добавлен')
            return redirect('product_detail', id=self.object.id)
        return self.render_to_response(self.get_context_data(form=form))

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    pk_url_kwarg = 'review_id'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

    def get_success_url(self):
        messages.success(self.request, "Review deleted successfully!")
        return reverse_lazy('product_detail', kwargs={'id': self.object.product.id})

# Простые страницы
class AboutView(TemplateView): template_name = 'products/about.html'
class ContactView(TemplateView): template_name = 'products/contact.html'