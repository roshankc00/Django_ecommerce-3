from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_email', 'address', 'postalNo', 'status', 'is_active', 'is_delivered')

    def get_user_email(self, obj):
        return obj.user.email if obj.user else 'N/A'

    get_user_email.short_description = 'User Email'

