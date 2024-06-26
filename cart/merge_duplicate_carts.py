from django.core.management.base import BaseCommand
from cart.models import Cart, CartItem
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Merge duplicate carts for each user'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            carts = Cart.objects.filter(user=user)
            if carts.count() > 1:
                main_cart = carts.first()
                for duplicate_cart in carts[1:]:
                    for item in duplicate_cart.items.all():
                        cart_item, created = CartItem.objects.get_or_create(cart=main_cart, product=item.product)
                        cart_item.total_quantity += item.total_quantity
                        cart_item.total_price += item.total_price
                        cart_item.save()
                    duplicate_cart.delete()
        self.stdout.write(self.style.SUCCESS('Successfully merged duplicate carts'))