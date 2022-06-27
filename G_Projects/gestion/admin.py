from django.contrib import admin
from .models import Project, Fournisseur, Grossiste, Partenaire, Teleacteur, Opportunite, ToDo


admin.site.register(Project)
admin.site.register(ToDo)
admin.site.register(Teleacteur)
admin.site.register(Fournisseur)
admin.site.register(Grossiste)
admin.site.register(Partenaire)
admin.site.register(Opportunite)
