from django.contrib import admin



# Register your models here.


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    ]
    list_display_links = [
        'user',
        'shipping_address',
    ]
    list_filter = ['user',
                   'ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']






class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slide)

