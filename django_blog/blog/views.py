from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404
import datetime
from .models import Post

def home_page(request):
    posts=Post.objects.all()
    template=loader.get_template('index.html')
    now=datetime.datetime.now()
    html=template.render(locals()).encode()
    return HttpResponse(html)

def show_post(request,post_name):
    template=loader.get_template('post.html')
    post=get_object_or_404(Post,slug=post_name)
    html=template.render(locals()).encode()
    return HttpResponse(html)

def post_like_post(request,post_name):
    post=get_object_or_404(Post,slug=post_name)
    post.like_count+=1
    post.save()
    return HttpResponseRedirect(reverse('blog:post', args=(post_name,)))
def post_dislike_post(request,post_name):
    post=get_object_or_404(Post,slug=post_name)
    post.like_count-=1
    post.save()
    return HttpResponseRedirect(reverse('blog:post', args=(post_name,)))
