from django.contrib import admin
from .models import TodoItems


@admin.register(TodoItems)
class TodoItemsAdmin(admin.ModelAdmin):
    list_display = "title", "is_complete"
    list_display_links = list_display
    pass