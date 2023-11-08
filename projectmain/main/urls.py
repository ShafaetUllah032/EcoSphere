from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('complain/', views.complain, name='complain'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='checkout'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('categories/<int:id>', views.category_view, name='category_view'),
    path('captions/<int:id>', views.caption_view, name='caption_view'),
    path('products/<int:id>', views.product_view, name='product_view'),
    # path('products/<str:code>', views.product_view, name='product_view'), #tried with code instead of id
    path('dynamic_products/<int:id>', views.dynamic_product_view, name='dynamic_product_view'),
]