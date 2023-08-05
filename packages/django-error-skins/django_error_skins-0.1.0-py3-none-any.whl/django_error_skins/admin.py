from django.contrib import admin

from .models import ErrorSkin


@admin.register(ErrorSkin)
class ErrorAdmin(admin.ModelAdmin):
    list_display = (
        "active",
        "theme",
    )
