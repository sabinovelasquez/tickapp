from django.contrib import admin

from .models import Premise, Premise_Category, Category, Drink

# class ChoiceInline(admin.StackedInline):
#     model = Category

# class DrinksInline(admin.StackedInline):
#   model = Drink

class CategoryInline(admin.StackedInline):
  model = Premise_Category

class PremiseAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,               {'fields': ['name']}),
      ('Info:', {'fields':['description', 'code']}),
      ('Registry information', {'fields': ['pub_date']}),
  ]
  inlines = [CategoryInline]
  list_display = ('name', 'code', 'pub_date')

# class DrinkAdmin(admin.ModelAdmin):
#   inlines = [CategoryInline]



admin.site.register(Premise, PremiseAdmin)
admin.site.register(Drink)
admin.site.register(Category)
admin.site.register(Premise_Category)