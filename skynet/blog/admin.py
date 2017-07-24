from django.contrib import admin
from blog import models
from django.contrib.auth.admin import UserAdmin


class BlogUserAdmin(UserAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time')

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category)
admin.site.register(models.BlogComment)
admin.site.register(models.User,BlogUserAdmin)