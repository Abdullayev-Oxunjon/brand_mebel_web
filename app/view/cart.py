from django.shortcuts import render, redirect

from app.models import Product, Cart, CartItem


def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_items = cart.cartitem_set.all()
        cart_total = sum(item.total for item in cart_items)
    else:
        cart_items = []
        cart_total = 0
    return render(request=request,
                  template_name='app/inpage/product/cart.html',
                  context={"cart_items": cart_items,
                           "cart_total": cart_total})


def add_cart_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()

    if request.method == "POST":
        quantity = request.POST['quantity']
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
        cart_item.quantity = cart_item.quantity - 1
        cart_item.quantity += int(quantity)
        cart_item.save()
        return redirect('cart')


def delete_cart(request, product_id):
    cart_item = CartItem.objects.filter(id=product_id, cart__user=request.user).first()
    if cart_item:
        cart_item.delete()
        return redirect("cart")


def edit_cart_view(request, product_id):
    try:
        cart_item = CartItem.objects.get(pk=product_id,
                                         cart__user=request.user)
        if request.method == "POST":
            quantity = int(request.POST['quantity'])
            cart_item.quantity = quantity
            cart_item.save()

        return redirect("cart")

    except CartItem.DoesNotExist:
        pass

    return redirect('cart')

# @login_required(login_url='login')
# def edit_cart_item_view(request, product_id):
#     try:
#         cart_item = CartItem.objects.get(pk=product_id,
#                                          cart__user=request.user)
#
#         if request.method == 'POST':
#             quantity = int(request.POST['quantity'])
#             cart_item.quantity = quantity
#             cart_item.save()
#
#         return redirect('product-cart-page')
#
#     except CartItem.DoesNotExist:
#         pass
#
#     return redirect('product-cart-page')
