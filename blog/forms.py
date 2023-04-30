from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Post # 사용할 모델
        fields = ['title','category','content'] # 폼에서 사용할 모델의 속성 
        # form 이름 지정
        labels = {
            'title': _('제목'),
            'category':_('카테고리'),
            'content':_('내용'),
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
        fields = ['image']
        labels = {
            'image': _('이미지'),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content':_('댓글내용'),
        }