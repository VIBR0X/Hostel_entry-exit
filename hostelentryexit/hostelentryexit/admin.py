from django.contrib import admin
from .models import Hostel
from .models import Database
from .models import users
from .models import tempdata

admin.site.register(Hostel)
admin.site.register(Database)
admin.site.register(users)
admin.site.register(tempdata)
