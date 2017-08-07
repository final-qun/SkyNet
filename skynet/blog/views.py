import simplejson as simplejson
from django.contrib import auth
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from blog.models import *


class IndexView(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        blogs = Blog.objects.filter(status='P')
        return blogs

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["blogs"] = self.get_queryset()
        return context


class UIndexView(ListView):
    template_name = "blog/user/uindex.html"
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


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'blog_id'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        blog_id = self.kwargs[self.pk_url_kwarg]
        blog = Blog.objects.get(pk=blog_id)
        comments = blog.blogcomment_set.all()
        context['comments'] = comments
        return context


class EditBlogView(DetailView):
    model = Blog
    template_name = 'blog/user/edit.html'
    pk_url_kwarg = 'blog_id'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(EditBlogView, self).get_context_data(**kwargs)
        blogs = self.request.user.blog_set.all()
        context['blogs'] = blogs
        return context


@csrf_exempt
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        userquery = User.objects.filter(Q(email=name) | Q(username=name))
        for user in userquery:
            if user is not None and user.check_password(pwd):
                auth.login(request, user)
                return HttpResponse(simplejson.dumps({'error': ''}, ensure_ascii=False))
        return HttpResponse(simplejson.dumps({'error': '用户不存在'}, ensure_ascii=False))
    return render(request, 'blog/login.html', {"islogin": True})


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
    return render(request, 'blog/login.html', {"islogin": False})


def create_blog(request):
    if request.user.is_authenticated:
        blog = Blog.objects.create(user=request.user)
        return HttpResponse(simplejson.dumps({'error': 0, 'id': blog.pk}, ensure_ascii=False))
    else:
        return HttpResponse(simplejson.dumps({'error': 1}, ensure_ascii=False))



@csrf_exempt
def save_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.title = request.POST.get('title')
    blog.body = request.POST.get('body')
    blog.save()
    return HttpResponse()


def pub_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.title = request.POST.get('title')
    blog.body = request.POST.get('body')
    blog.status = 'P'
    blog.save()
    return render(request, 'blog/u/' + str(request.user.pk))


def delete_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    return HttpResponseRedirect("/blog/u/" + str(request.user.pk))


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect("/blog")
