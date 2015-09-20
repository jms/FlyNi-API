# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Website, Fly, Item

class ItemInline(admin.TabularInline):
    '''
    Tabular Inline View for Item
    '''
    model = Item
    min_num = 3
    max_num = 20
    extra = 1


class FlyAdmin(admin.ModelAdmin):
    '''
        Admin View for Fly
    '''
    list_display = ('create_date',)
    list_filter = ('create_date',)
    inlines = [
        ItemInline,
    ]

admin.site.register(Website)
admin.site.register(Fly, FlyAdmin)
