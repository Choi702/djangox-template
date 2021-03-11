from django.urls import path

from .views import RetailListView, RetailCreateView, RetailUpdateView, RetailDeleteView, RetailDetailView

urlpatterns = [
    path('', RetailListView.as_view(), name='retail_list'),
    path('<int:pk>/', RetailDetailView.as_view(), name='retail_detail'),
    path('new/', RetailCreateView.as_view(), name='retail_create'),
    path('<int:pk>/edit', RetailUpdateView.as_view(), name='retail_update'),
    path('<int:pk>/delete', RetailDeleteView.as_view(), name='retail_delete'),
]
