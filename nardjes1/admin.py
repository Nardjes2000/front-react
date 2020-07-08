from django.contrib import admin
from .models import malade,dossier,grocess,antcf,antcp,info_naissance

# Register your models here.
class maladeAdmin(admin.ModelAdmin):  # add this
      list_display = ('nom','prenom','telephone','date','csg')


      
admin.site.register(malade)
admin.site.register(dossier)
admin.site.register(grocess)
admin.site.register(antcp)
admin.site.register(antcf)
admin.site.register(info_naissance)
