from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', )
        # form 이름 지정
        labels = {
            'title': _('Title'),
            'content':_('Content')
        }
        # 제목이 10자가 넘어가면 에러메세지를 띄워줌. 
        error_messages = {
            'Title': {
                'max_length': _("제목은 10자이내로 가능합니다."),
            },
        }
 
 
class ImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image', )
        labels = {
            'image': _('Image'),
            
        }