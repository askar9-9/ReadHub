from django.contrib import admin
from .models import Library
# Register your models here.
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    # Отображаемые данные
    list_display = ['owner', 'book', 'status', 'pages_read', 'date_added']
    