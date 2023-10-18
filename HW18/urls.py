from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('item/new/', ItemCreateView.as_view(), name='item_new'),
    path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
