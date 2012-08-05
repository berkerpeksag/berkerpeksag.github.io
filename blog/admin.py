from blog.models import Post
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('pub_date', 'update_date')

admin.site.register(Post, PostAdmin)
