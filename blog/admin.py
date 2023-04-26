from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']
# Register your models here.
admin.site.register(Post,PostAdmin)