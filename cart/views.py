from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import Product
from .models import Cart, CartItem

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.total_quantity += 1
    cart_item.save()
    cart.save()  # Сохранение корзины для обновления итоговых значений
    return redirect('cart:cart_detail')

@require_POST
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    carts = Cart.objects.filter(user=user)
    if carts.exists():
        cart = carts.first()
    else:
        cart = Cart.objects.create(user=user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    cart.save()  # Сохранение корзины для обновления итоговых значений
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart_detail.html', {'cart': cart})