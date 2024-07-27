from django.contrib import admin
from .models import Post , Comment
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug', 'body', 'pub_date', 'created_at', 'updated', 'status' ]
  list_filter = ['status', 'created_at','pub_date','author']
  search_fields = ['title', 'body']
  # autofill based on address 
  prepopulated_fields = {'slug':('title',)}
  # raw_id_fields= ['author']
  autocomplete_fields = ['author']
  # year and month
  date_hierarchy = 'pub_date'
  # admin order + -
  ordering = ['status', 'pub_date']  



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['name','email','post','created','active']
  list_filter = ['active', 'created', 'updated']
  search_fields = ['name', 'email','body']
  
