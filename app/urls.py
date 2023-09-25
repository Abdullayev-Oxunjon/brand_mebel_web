from django.urls import path

from app.views import index_view, shop_view, new_arrials, blog_view, blog_details, product_single, contact, about

urlpatterns = [
    path('', index_view, name='index'),
    path('shop/', shop_view, name='shop'),
    path('new_arrials/', new_arrials, name='new_arrials'),
    path('blog/', blog_view, name='blog'),
    path('blog-details/', blog_details, name='blog-details'),
    path('product-single/', product_single, name='product-single'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
