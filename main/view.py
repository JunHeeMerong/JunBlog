from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    # 유저의 포스트개수 세기
    if request.user in User.objects.all(): # 유저가 로그인하면
        posts = Post.objects.filter(author_id=request.user).count() # 유저의 아이디=포스트 작성자 아이디 인 포스트들의 갯수를 세서 posts에 담아서 render
    else:
        posts = Post.objects
    context = {'posts':posts}
    return render(request, 'main/main.html',context)