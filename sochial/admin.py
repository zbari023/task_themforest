from django.contrib import admin

# Register your models here.
from .models import Post , Comment




class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_date']
    list_filter = ['user', 'create_date']
    search_fields = ['user']
    

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
