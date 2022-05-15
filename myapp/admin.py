from django.contrib import admin
from .models import cons
from .models import comment
from .models import location
from .models import location_two



# Register your models here.

admin.site.register(cons)
admin.site.register(comment)
admin.site.register(location)
admin.site.register(location_two)

