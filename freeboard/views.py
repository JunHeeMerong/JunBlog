from django.shortcuts import render, get_object_or_404, redirect,resolve_url
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import modelformset_factory
from django.utils import timezone
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.contrib import messages

from blog.models import *
from .models import *
from .forms import *

# 유저의 게시글수 확인
def countpost(request):
    if request.user in User.objects.all(): # 유저가 로그인하면
        postcount = Post.objects.filter(author_id=request.user).count()
        freepostcount = FreePost.objects.filter(author_id=request.user).count()
        return postcount+freepostcount # 유저의 아이디=포스트 작성자 아이디 인 포스트들의 갯수를 세서 posts에 담아서 render

# 유저의 댓글수 확인
def countcomment(request):
    if request.user in User.objects.all():
        commentcount = Comment.objects.filter(author_id=request.user).count()
        freecommentcount = FreeComment.objects.filter(author_id=request.user).count()
        return commentcount+freecommentcount
    
    
# 자유게시판 홈
def freeboardhome(request):
    # 유저의 포스트개수 세기
    posts = countpost(request)
    comments = countcomment(request)
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    freepost_list = FreePost.objects.order_by('-create_date')
    if kw:
        freepost_list = freepost_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(freecomment__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(freecomment__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(freepost_list, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'posts':posts,'comments':comments}
    return render(request, 'freeboard/freeboardmain.html', context)

# 자유게시판 상세페이지
def free_detail(request, freepost_id):
    freepost = get_object_or_404(FreePost, pk=freepost_id)
    comments = countcomment(request)
    posts = countpost(request)
    context = {'post': freepost,'posts':posts,'comments':comments}
    return render(request, 'freeboard/freeboard_detail.html', context)

# 자유게시판 글쓰기
def free_post_create(request):
    posts = countpost(request)
    comments = countcomment(request)
    #하나의 모델폼을 여러번 쓸수 있음. 모델,모델폼,몇개의 폼을 띄울건지 갯수
    FreeImageFormSet = modelformset_factory(FreePostImage,form=FreeImageForm,extra=3)
    if request.method=='POST':
        freepostform = FreePostForm(request.POST)
        # queryset을 none으로 정의해서 이미지가 없어도 되도록 설정. none은 빈 쿼리셋 리턴
        freeformset = FreeImageFormSet(request.POST, request.FILES, queryset=FreePostImage.objects.none())
        if freepostform.is_valid() and freeformset.is_valid():
            freepost_form = freepostform.save(commit=False) # 임시저장
            freepost_form.author = request.user
            freepost_form.create_date = timezone.now()
            freepost_form.save()
            for form in freeformset.cleaned_data:
                if form:
                    freeimage = form['freeimage']
                    photo = FreePostImage(freepost=freepost_form,freeimage=freeimage)
                    photo.save()
            return redirect('freeboard:freeboardhome')
        else:
            print(freepostform.errors,freeformset.errors)
    else:
        freepostform = FreePostForm()
        freeformset = FreeImageFormSet(queryset=FreePostImage.objects.none()) # 이미지폼
    context = {'postform':freepostform,'formset':freeformset,'posts':posts,'comments':comments}
    return render(request,'freeboard/freeboard_form.html',context)

# 자유게시판 수정
def free_post_modify(request, freepost_id):
    freepost = get_object_or_404(FreePost, pk=freepost_id)
    posts = countpost(request)
    comments = countcomment(request)
    FreeImageFormSet = modelformset_factory(FreePostImage,form=FreeImageForm,extra=10)
    if request.user != freepost.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('freeboard:free_detail', freepost_id=freepost.id)
    if request.method == "POST":
        freepostform = FreePostForm(request.POST, instance=freepost)
        formset = FreeImageFormSet(request.POST, request.FILES, queryset=FreePostImage.objects.none())
        if freepostform.is_valid():
            freepost_form = freepostform.save(commit=False)
            freepost_form.modify_date = timezone.now()  # 수정일시 저장
            freepost_form.save()
            for form in formset.cleaned_data:
                if form:
                    freeimage = form['freeimage']
                    photo = FreePostImage(freepost=freepost_form,freeimage=freeimage)
                    photo.save()
            return redirect('freeboard:free_detail',freepost_id=freepost.id)
    else:
        freepostform = FreePostForm(instance=freepost)
        formset = FreeImageFormSet(queryset=FreePostImage.objects.none()) # 이미지폼
    context = {'postform':freepostform,'formset':formset,'posts':posts,'comments':comments}
    return render(request, 'freeboard/freeboard_form.html', context)

# 자유게시판 삭제
def free_post_delete(request, freepost_id):
    freepost = get_object_or_404(FreePost, pk=freepost_id)
    if request.user != freepost.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('freeboard:free_detail', freepost_id=freepost.id)
    freepost.delete()
    return redirect('freeboard:freeboardhome')

# 댓글작성
def free_comment_create(request, freepost_id):
    freepost = get_object_or_404(FreePost, pk=freepost_id)
    if request.method == "POST":
        form = FreeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # author 속성에 로그인 계정 저장
            comment.create_date = timezone.now()
            comment.freepost = freepost
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('freeboard:free_detail', freepost_id=freepost.id), comment.id))
    else:
        form = FreeCommentForm()
    context = {'post': freepost, 'form': form}
    return render(request, 'freeboard/freeboard_detail.html', context)

# 댓글 수정
def free_comment_modify(request, comment_id):
    comment = get_object_or_404(FreeComment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('freeboard:free_detail', freepost_id=comment.freepost.id)
    if request.method == "POST":
        form = FreeCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('freeboard:free_detail', freepost_id=comment.freepost.id), comment.id))
    else:
        form = FreeCommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'freeboard/free_comment_form.html', context)

# 댓글 삭제
def free_comment_delete(request, comment_id):
    comment = get_object_or_404(FreeComment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('freeboard:free_detail', freepost_id=comment.freepost.id)