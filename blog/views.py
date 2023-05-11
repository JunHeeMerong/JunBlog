from django.shortcuts import render, get_object_or_404, redirect,resolve_url
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import modelformset_factory
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages

from freeboard.models import *
from .models import *
from .forms import PostForm,ImageForm,CommentForm

# 유저의 게시글수 확인
def countpost(request):
    if request.user in User.objects.all(): # 유저가 로그인하면
        postcount = Post.objects.filter(author_id=request.user).count() # Post모델에서 유저아이디랑 접속아이디가 같은 것들 갯수세기
        freepostcount = FreePost.objects.filter(author_id=request.user).count() # FreePost모델에서 유저아이디랑 접속아이디가 같은 것들 갯수세기
        return postcount+freepostcount # 블로그 작성글과 자유게시판 작성글 갯수의 합 계산

# 유저의 댓글수 확인
def countcomment(request):
    if request.user in User.objects.all():
        commentcount = Comment.objects.filter(author_id=request.user).count() # Comment모델에서 유저아이디랑 접속아이디가 같은 것들 갯수세기
        freecommentcount = FreeComment.objects.filter(author_id=request.user).count() # FreeComment모델에서 유저아이디랑 접속아이디가 같은 것들 갯수세기
        return commentcount+freecommentcount # 블로그 작성댓글과 자유게시판 작성댓글 갯수의 합 계산
    
# 블로그홈
def bloghome(request):
    # 유저의 포스트개수 세기
    posts = countpost(request)
    comments = countcomment(request)
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    cg = request.GET.get('cg','') # 카테고리
    post_list = Post.objects.order_by('-create_date')
    countcategory = []
    for i in range(1,Category.objects.count()+1):
        countcategory.append(post_list.filter(category_id=i).count())
    if kw: # 검색기능 필터
        post_list = post_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(comment__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(comment__author__username__icontains=kw) |  # 답변 글쓴이 검색
            Q(category__name__icontains=kw) # 카테고리로도 검색
        ).distinct()
    if cg: # 카테고리 필터
        post_list = post_list.filter(Q(category__name__icontains=cg))
    paginator = Paginator(post_list, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    category = Category.objects.all()
    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'posts':posts,'comments':comments,'countcategory':countcategory,'category':category}
    return render(request, 'blog/blogmain.html', context)

# 블로그 상세페이지
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = countcomment(request)
    posts = countpost(request)
    post_list = Post.objects.order_by('-create_date')
    countcategory = []
    for i in range(1,Category.objects.count()+1):
        countcategory.append(post_list.filter(category_id=i).count())
    context = {'post': post,'posts':posts,'comments':comments,'countcategory':countcategory}
    return render(request, 'blog/post_detail.html', context)

# 블로그 글쓰기
def post_create(request):
    posts = countpost(request)
    comments = countcomment(request)
    #하나의 모델폼을 여러번 쓸수 있음. 모델,모델폼,몇개의 폼을 띄울건지 갯수
    ImageFormSet = modelformset_factory(PostImage,form=ImageForm,extra=3)
    if request.method=='POST':
        postform = PostForm(request.POST)
        # queryset을 none으로 정의해서 이미지가 없어도 되도록 설정. none은 빈 쿼리셋 리턴
        formset = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())
        if postform.is_valid() and formset.is_valid():
            post_form = postform.save(commit=False) # 임시저장
            post_form.author = request.user
            post_form.create_date = timezone.now()
            post_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = PostImage(post=post_form,image=image)
                    photo.save()
            return redirect('blog:bloghome')
        else:
            print(postform.errors,formset.errors)
    else:
        postform = PostForm()
        formset = ImageFormSet(queryset=PostImage.objects.none()) # 이미지폼
    post_list = Post.objects.order_by('-create_date')
    countcategory = []
    for i in range(1,Category.objects.count()+1):
        countcategory.append(post_list.filter(category_id=i).count())
    context = {'postform':postform,'formset':formset,'posts':posts,'comments':comments,'countcategory':countcategory}
    return render(request,'blog/post_form.html',context)

# 블로그 수정
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts = countpost(request)
    comments = countcomment(request)
    ImageFormSet = modelformset_factory(PostImage,form=ImageForm,extra=10)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('blog:detail', post_id=post.id)
    if request.method == "POST":
        postform = PostForm(request.POST, instance=post)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())
        if postform.is_valid():
            post_form = postform.save(commit=False)
            post_form.modify_date = timezone.now()  # 수정일시 저장
            post_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = PostImage(post=post_form,image=image)
                    photo.save()
            return redirect('blog:detail',post_id=post.id)
    else:
        postform = PostForm(instance=post)
        formset = ImageFormSet(queryset=PostImage.objects.none()) # 이미지폼
    post_list = Post.objects.order_by('-create_date')
    countcategory = []
    for i in range(1,Category.objects.count()+1):
        countcategory.append(post_list.filter(category_id=i).count())
    context = {'postform':postform,'formset':formset,'posts':posts,'comments':comments,'countcategory':countcategory}
    return render(request, 'blog/post_form.html', context)

# 블로그 삭제
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('blog:detail', post_id=post.id)
    post.delete()
    return redirect('blog:bloghome')

# 댓글작성
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # author 속성에 로그인 계정 저장
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('blog:detail', post_id=post.id), comment.id))
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'blog/post_detail.html', context)

# 댓글 수정
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('blog:detail', post_id=comment.post.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('blog:detail', post_id=comment.post.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'blog/comment_form.html', context)

# 댓글 삭제
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('blog:detail', post_id=comment.post.id)