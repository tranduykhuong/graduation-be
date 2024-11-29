from django.contrib import admin
from django.utils.html import format_html
from django.forms import Textarea
from .models import Wisher

@admin.register(Wisher)
class WisherAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'email', 'relationship', 'confirm', 'is_active', 'img_display')
    list_filter = ('confirm', 'is_active')
    search_fields = ('name', 'email', 'key', 'relationship')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('key', 'last3phone', 'name', 'email', 'relationship', 'img_url', 'wisher', 'confirm', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'wisher':
            kwargs['widget'] = Textarea(attrs={'rows': 5, 'cols': 80})
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def img_display(self, obj):
        """Custom method to display an image thumbnail in the list view."""
        if obj.img_url:
            return format_html('<img src="{}" width="50" />', obj.img_url)
        return "No Image"

    img_display.short_description = "Image"
