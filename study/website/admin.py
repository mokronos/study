from django.contrib import admin

# Register your models here.

from reversion_compare.admin import CompareVersionAdmin

from .models import Post

@admin.register(Post)
class PostAdmin(CompareVersionAdmin):
    pass
