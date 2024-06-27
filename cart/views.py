from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product



@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.total_quantity += quantity
            cart_item.save()
        else:
            cart_item.total_quantity = quantity
            cart_item.save()

    return redirect('product_detail', product_id=product_id)