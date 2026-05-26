from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Productos CRUD
    path('products/create/', views.product_create, name='product_create'),
    path('products/<uuid:pk>/edit/', views.product_update, name='product_update'),
    path('products/<uuid:pk>/delete/', views.product_delete, name='product_delete'),

    # Cart
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<uuid:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<uuid:item_id>/', views.update_cart_item, name='update_cart_item'),
]