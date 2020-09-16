from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404
import datetime
from . import models

def home_page(request):
    posts=models.Post.objects.all()
    template=loader.get_template('index.html')
    now=datetime.datetime.now()
    html=template.render(locals()).encode()
    return HttpResponse(html)

def show_post(request,post_slug):
    template=loader.get_template('post.html')
    post=get_object_or_404(models.Post,slug=post_slug)
    html=template.render(locals()).encode()
    return HttpResponse(html)

def post_like_post(request,post_slug):
    post=get_object_or_404(models.Post,slug=post_slug)
    post.like_count+=1
    post.save()
    return HttpResponseRedirect(reverse('mainsite:post', args=(post_slug,)))
def post_dislike_post(request,post_slug):
    post=get_object_or_404(models.Post,slug=post_slug)
    post.like_count-=1
    post.save()
    return HttpResponseRedirect(reverse('mainsite:post', args=(post_slug,)))


def video(request,video_slug='first'):
    template=loader.get_template('video_index.html')
    video_list=models.Video.objects.all()
    now=datetime.datetime.now()
    if video_slug=='first':
        return HttpResponseRedirect(reverse('mainsite:video', args=(video_list[0].slug,)))
    else:
        video=get_object_or_404(models.Video,slug=video_slug)
        html=template.render(locals()).encode()
        return HttpResponse(html)


def sum(request,a,b):
    html=str(a)+'+'+str(b)+'='+str(a+b)
    return HttpResponse(html)
def trans(request,n,type):
    if type=='cm':
        html=str(n)+type+'='+str(round(n/2.54,2))+'in'
    if type=='in':
        html=str(n)+type+'='+str(round(n*2.54,2))+'cm'
    return HttpResponse(html)