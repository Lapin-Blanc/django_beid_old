from django.contrib import admin
from groupes.models import Groupe

class GroupeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'apercu_membres',)
    filter_horizontal = ('membres',)
# Register your models here.

admin.site.register(Groupe, GroupeAdmin)
