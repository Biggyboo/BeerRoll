import django.contrib.admin as admin
import BeerRollAPI.models as models


# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'description',
        'get_category',
        'get_origin',
        'alcohol_level',
        'price',
        'bitterness'
    )

    def get_category(self, obj):
        return obj.category.label

    get_category.short_description = 'category'
    get_category.admin_order_field = 'category'

    def get_origin(self, obj):
        return obj.origin.label

    get_origin.short_description = 'origin'
    get_origin.admin_order_field = 'origin'


class BeerQuantityAdmin(admin.ModelAdmin):
    list_display = ('get_beer', 'get_quantity', 'stock')

    def get_beer(self, obj):
        return obj.beer.label

    get_beer.short_description = 'beer'
    get_beer.admin_order_field = 'beer'

    def get_quantity(self, obj):
        return obj.quantity.quantity

    get_quantity.short_description = 'quantity'
    get_quantity.admin_order_field = 'quantity'


admin.site.register(models.Beer, BeerAdmin)
admin.site.register(models.Origin)
admin.site.register(models.Category)
admin.site.register(models.Quantity)
admin.site.register(models.BeerQuantity, BeerQuantityAdmin)
