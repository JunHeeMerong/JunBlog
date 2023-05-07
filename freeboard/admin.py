from django.contrib import admin
from .models import FreePost,FreePostImage

class InlineFreePostImage(admin.TabularInline):
    model = FreePostImage

class FreePostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [InlineFreePostImage]
    def save_model(self, request, obj, form, change):
    	# super().save_model(request, obj, form, change)
        obj.save()
        for img in request.FILES.getlist('images'):
            obj.postimage_set.create(image_url=img)

# Register your models here.
admin.site.register(FreePost,FreePostAdmin)