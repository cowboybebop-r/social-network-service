from django.contrib import admin
from .models import Post, PostRate


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostRate)
class PostRateAdmin(admin.ModelAdmin):
    pass
