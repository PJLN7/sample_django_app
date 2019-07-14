# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TodoItem


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('content',)
# define ItemAdmin class and use list_display to display fields


admin.site.register(TodoItem, ItemAdmin)
# to manage our models from admin, register the model