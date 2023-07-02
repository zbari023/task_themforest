from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Post , Comment






class PostAdmin(SummernoteModelAdmin):
    list_display = ['user', 'create_date']
    list_filter = ['user', 'create_date']
    search_fields = ['user']
    summernote_fields = '__all__'
    

admin.site.register(Post, PostAdmin )
admin.site.register(Comment)
