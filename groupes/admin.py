from django.contrib import admin
from groupes.models import Groupe

class GroupeAdmin(admin.ModelAdmin):
    filter_horizontal = ('membres',)
# Register your models here.

admin.site.register(Groupe, GroupeAdmin)
