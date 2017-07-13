import simplejson as simplejson
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from markdown2 import markdown

from blog.models import *
from blog.froms import *


class IndexView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


class EditPostView(ListView):
    model = Blog
    template_name = 'edit.html'
    context_object_name = 'posts'

def login(request):
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            data = lf.cleaned_data
            print(data)
            email = data['email']
            pwd = data['pwd']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return HttpResponseRedirect('/blog/login/')
            if user and  user.check_password(pwd):
                response = HttpResponseRedirect('/blog/')
                response.set_cookie('email',email,3600)
                return response
        return HttpResponseRedirect('/blog/login/')
    else:
        lf = LoginForm()
    return render(request, 'login.html', {'lf':lf})

def register(request):
    if request.method == 'POST':
        rf = RegisterForm(request.POST)
        if rf.is_valid():
            data = rf.cleaned_data
            print(data)
            name = data['name']
            email = data['email']
            pwd = data['pwd']
            pwd2 = data['pwd2']
            user = User.objects.filter(Q(email__exact=email)|Q(username=name))
            if pwd2 == pwd and not user:
                user = User()
                user.username = name
                user.set_password(pwd)
                user.email = email
                user.save()
                response = HttpResponseRedirect('/blog/')
                response.set_cookie('email', email, 3600)
                return response
        return HttpResponseRedirect('/blog/register/')
    else:
        rf = RegisterForm()
    return render(request, 'register.html', {'rf':rf})

@csrf_exempt
def add_new_post(request):
    print('add new post')
    post = Blog.objects.create(title='无标题文章',
                                   body='',
                                   status='1',
                                   category=None)
    return HttpResponse(simplejson.dumps({'id':post.pk,
                                    'title':post.title}, ensure_ascii=False))


@csrf_exempt
def show_post(request, post_id):
    post = Blog.objects.get(pk=post_id)
    return HttpResponse(simplejson.dumps({'body': post.body,
                                          'title': post.title}, ensure_ascii=False))


@csrf_exempt
def save_post(request, post_id):
    print('savePost')
    post = Blog.objects.get(pk=post_id)
    print(post.title,post.body)
    if request.is_ajax():
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')
        print(post.title, post.body)
        post.save()
    return HttpResponse()