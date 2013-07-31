from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('pub_date', 'update_date')

admin.site.register(Post, PostAdmin)
