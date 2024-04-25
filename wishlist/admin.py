from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_products_count')

    def get_products_count(self, obj):
        return obj.products.count()

    get_products_count.short_description = 'Products Count'

