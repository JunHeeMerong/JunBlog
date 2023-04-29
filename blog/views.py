from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

# Create your views here.
def index(request):
    return HttpResponse("test")

def bloghome(request):
    # ImageFormSet = modelformset_factory(PostImage,form=ImageForm, extra=3)
    # if request.method == 'POST':
        
    #     postForm = PostForm(request.POST)
    #     # queryset 을 none 으로 정의해서 이미지가 없어도 되도록 설정. none 은 빈 쿼리셋 리턴
    #     formset = ImageFormSet(request.POST, request.FILES,
    #                            queryset=PostImage.objects.none())
    
    #     # 두 모델폼의 유효성 검사를 해주고
    #     if postForm.is_valid() and formset.is_valid():
    #         # 저장을 잠시 멈추고
    #         post_form = postForm.save(commit=False)
    #         # Post user 에 현재 요청된 user 를 담아서 
    #         post_form.user = request.user
    #         # 저장. 이 작업 안하면 user null error
    #         post_form.save()
    #         # 유효성 검사가 왼료된 formset 정리된 데이터 모음
    #         for form in formset.cleaned_data:
               
    #             if form:
    #                 # image file 
    #                 image = form['image']
    #                 # F.K post, image file save
    #                 photo = PostImage(post=post_form, image=image)
    #                 photo.save()
    #         # index url 로 return
    #         return HttpResponseRedirect("/")
    #     # 유효성 검사 실패시 에러메세지를 터미널상에 print
    #     else:
    #         print(postForm.errors, formset.errors)
    # else:
    #     # POST 요청이 아닌 경우 
    #     postForm = PostForm()
    #     formset = ImageFormSet(queryset=PostImage.objects.none())
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    post_list = Post.objects.order_by('-create_date')
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj, 'page': page, 'kw': kw} # ,'postForm': postForm, 'formset': formset
    return render(request, 'blog/blogmain.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)