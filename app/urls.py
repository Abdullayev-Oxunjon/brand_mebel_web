from django.urls import path

from app.view.auth import register_view, login_view
from app.view.other import index_view, shop_view, new_arrials, blog_view, blog_details, product_single, contact, about, \
    my_account, checkout, cart, wishlist

urlpatterns = [
    path('', index_view, name='index'),
    path('shop/', shop_view, name='shop'),
    path('new_arrials/', new_arrials, name='new_arrials'),
    path('blog/', blog_view, name='blog'),
    path('blog-details/<int:blog_id>/', blog_details, name='blog-details'),
    path('product-single/<int:product_id>/', product_single, name='product-single'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('my_account/', my_account, name='my_account'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),

]
