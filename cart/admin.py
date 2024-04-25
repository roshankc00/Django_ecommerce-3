from django.contrib import admin
from .models import CartItem, Cart

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('get_cart_user', 'quantity', 'product')

    def get_cart_user(self, obj):
        return obj.cart.user.email if obj.cart.user else 'N/A'

    get_cart_user.short_description = 'User'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('get_cart_user', 'get_cart_items_count')

    def get_cart_user(self, obj):
        return obj.user.email if obj.user else 'N/A'

    get_cart_user.short_description = 'User'

    def get_cart_items_count(self, obj):
        return obj.cart_items.count()

    get_cart_items_count.short_description = 'Cart Items Count'
