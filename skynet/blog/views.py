import simplejson as simplejson
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from blog.models import *


class IndexView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'


class UIndexView(ListView):
    template_name = "blog/index.html"
    page_kwarg = "user_id"

    def get_queryset(self):
        user_id = self.kwargs[self.page_kwarg]
        user = User.objects.get(pk=user_id)
        blogs = user.blog_set.all()
        return blogs

    def get_context_data(self, **kwargs):
        context = super(UIndexView, self).get_context_data(**kwargs)
        context["blogs"] = self.get_queryset()
        return context


class PostDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


class EditPostView(DetailView):
    model = Blog
    template_name = 'blog/edit.html'
    pk_url_kwarg = 'blog_id'
    context_object_name = 'blog'


@csrf_exempt
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        userquery = User.objects.filter(Q(email=name)|Q(username=name))
        for user in userquery:
            if user is not None and user.check_password(pwd):
                auth.login(request, user)
                return HttpResponse(simplejson.dumps({'error': ''}, ensure_ascii=False))
        return HttpResponse(simplejson.dumps({'error': '用户不存在'}, ensure_ascii=False))
    return render(request, 'blog/login.html',{"islogin":True})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        pwd2 = request.POST.get('pwd2')
        if pwd != pwd2:
            return HttpResponse(simplejson.dumps({'field': 'pwd2',
                                                  'error': '两次输入密码不一致'}, ensure_ascii=False))
        fileruser = User.objects.filter(Q(username=name) | Q(email__exact=email))
        if len(fileruser) > 0:
            return HttpResponse(simplejson.dumps({'field': 'name',
                                                  'error': '用户名已存在'}, ensure_ascii=False))
        user = User.objects.create_user(username=name, password=pwd, email=email)
        user.save()
        auth.login(request, user)
        return HttpResponse(simplejson.dumps({'error': ''}, ensure_ascii=False))
    return render(request, 'blog/login.html',{"islogin":False})


def create_blog(request):
    if request.user.is_authenticated:
        post = Blog.objects.create(title='',
                                   body='',
                                   status='E',
                                   user=request.user)
        return HttpResponse(simplejson.dumps({'error': 0, 'id': post.pk}, ensure_ascii=False))
    else:
        return HttpResponse(simplejson.dumps({'error': 1}, ensure_ascii=False))


@csrf_exempt
def show_post(request, post_id):
    post = Blog.objects.get(pk=post_id)
    return HttpResponse(simplejson.dumps({'body': post.body,
                                          'title': post.title}, ensure_ascii=False))

@csrf_exempt
def save_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.title = request.POST.get('title')
    blog.body = request.POST.get('body')
    print(blog.title,blog.body)
    blog.save()
    return HttpResponse()


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect("/blog");
