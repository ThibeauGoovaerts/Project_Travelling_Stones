from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Calloux
from .models import Pays
from .models import Personne

admin.site.register(Pays)
admin.site.register(Personne, UserAdmin)
admin.site.register(Calloux)
