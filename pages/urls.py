from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about_us"),
    path('items', views.item_list, name='item_list'),
    path('items/export', views.export_data, name='export_list'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_edit'),
    path('item/new/', views.ItemCreateView.as_view(), name='item_new'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
]
