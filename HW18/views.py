from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from django.urls import reverse_lazy

# Представление для списка объектов
class ItemListView(ListView):
    model = Item
    template_name = 'HW18/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'HW18/item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    fields = ['name']
    template_name = 'HW18/item_form.html'

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name']
    template_name = 'HW18/item_form.html'

    def get_success_url(self):
        return reverse_lazy('item-edit', args=[str(self.object.id)])

# Представление для удаления объекта
class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('item_list')
    template_name = 'HW18/item_confirm_delete.html'

class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'description']
    success_url = reverse_lazy('item_list')