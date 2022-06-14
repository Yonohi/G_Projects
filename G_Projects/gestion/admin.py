from django.contrib import admin
from .models import Project, Teleacteur, Lead, Nursering, FicheInfo


admin.site.register(Project)
admin.site.register(Teleacteur)
admin.site.register(Lead)
admin.site.register(Nursering)
admin.site.register(FicheInfo)
