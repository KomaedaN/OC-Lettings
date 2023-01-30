from django.contrib import admin

from .models import Letting
from .models import Address
from .models import Profile


class AddressAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Address'


admin.site.register(Letting)
admin.site.register(Address, AddressAdmin)
admin.site.register(Profile)
