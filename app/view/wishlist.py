from django.shortcuts import render, get_object_or_404, redirect

from app.models import Wishlist, Product


def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user).first()
    products = wishlist.product.all()

    return render(request=request,
                  template_name='app/inpage/product/wishlist.html',
                  context={"products": products})


def add_wishlist(request, product_id):
    product = get_object_or_404(klass=Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.product.add(product)
    return redirect("wishlist")


def delete_wishlist(request, product_id):
    product = get_object_or_404(klass=Product, id=product_id)
    wishlist = Wishlist.objects.filter(user=request.user).first()
    wishlist.product.remove(product)
    return redirect("wishlist")
