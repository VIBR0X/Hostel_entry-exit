from django.contrib import admin
from .models import Hostel
from .models import Database
from .models import users

class usersAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']

admin.site.register(Hostel)
admin.site.register(Database)
admin.site.register(users, usersAdmin)

