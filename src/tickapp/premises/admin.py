from django.contrib import admin

from .models import Premise, Category, Drink

class PremiseAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,               {'fields': ['name']}),
      ('Info:', {'fields':['description', 'code']}),
      ('Registry information', {'fields': ['pub_date']}),
  ]
  list_display = ('name', 'code', 'pub_date')

admin.site.register(Premise, PremiseAdmin)
admin.site.register(Drink)
admin.site.register(Category)