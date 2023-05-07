from django.contrib import admin
from .models import Post,Category,PostImage

class InlinePostImage(admin.TabularInline):
    model = PostImage

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [InlinePostImage]
    def save_model(self, request, obj, form, change):
    	# super().save_model(request, obj, form, change)
        obj.save()
        for img in request.FILES.getlist('images'):
            obj.postimage_set.create(image_url=img)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)