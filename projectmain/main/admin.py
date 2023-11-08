from django.contrib import admin
from .models import MainCarousel, OfferCarousel, Categories, Captions, Product, Contact, Cont_info, Dynamic_Product, Order, OrderUpdate


admin.site.register(MainCarousel)
admin.site.register(OfferCarousel)
admin.site.register(Categories)
admin.site.register(Captions)
admin.site.register(Contact)
admin.site.register(Cont_info)
admin.site.register(Dynamic_Product)
admin.site.register(OrderUpdate)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "order_id")



