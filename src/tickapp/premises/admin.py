from django.contrib import admin

from .models import Premise, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PremiseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Info:', {'fields':['description', 'code']}),
        ('Registry information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('name', 'code', 'pub_date')
admin.site.register(Premise, PremiseAdmin)
admin.site.register(Choice)
