from django.views.generic import ListView
from .models import ClothesModel, Brand

class ClothesListView(ListView):
    model = ClothesModel
    template_name = 'clothes.html'
    context_object_name = 'clothes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context

    def get_queryset(self):
        brand_id = self.request.GET.get('brand')
        if brand_id:
            return ClothesModel.objects.filter(brands_name__id=brand_id)
        return ClothesModel.objects.all()