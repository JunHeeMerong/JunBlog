from django.shortcuts import render,redirect
from blog.models import Post,Comment
from freeboard.models import *
from django.contrib.auth.models import User
from .programmers import progarmmers
import logging
logger = logging.getLogger('junblog')

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

# Create your views here. -----------------------------------------------------------------------
def home(request):
    # 유저의 포스트개수 세기
    logger.info("INFO 레벨로 출력")
    posts = countpost(request)
    comments = countcomment(request)
    context = {'posts':posts,'comments':comments}
    return render(request, 'main/main.html',context)

def programmers(request):
    if request.method == "POST":
        id = request.POST['id']
        pw = request.POST['pw']
        score = progarmmers(id,pw)
        context = {'score':score}
    else:
        context = {}
    return render(request, 'main/programmers.html',context)