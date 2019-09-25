from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

def home_page(request):
    posts=Post.objects.all()
    post_list=[]
    for count,post in enumerate(posts):
        post_list.append('No.'+str(count+1)+'\t'+post.title+'<br>')
        post_list.append(post.slug+'<hr>')
        post_list.append('<pre>'+str(count+1)+post.body+'</pre><br><br>')
    return HttpResponse(post_list)