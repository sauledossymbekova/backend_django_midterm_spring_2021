from django.contrib import admin

from main.models import Todo, Task


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    ordering = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'due', 'owner', 'todo']
    ordering = ['name']
    search_fields = ['name', 'owner__first_name', 'todo__name', ]
    list_filter = ['created', 'due', ]

