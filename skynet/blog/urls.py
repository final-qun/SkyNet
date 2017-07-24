from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^detail/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='detail'),
    url(r'^login/', csrf_exempt(login), name='login'),
    url(r'^register/', csrf_exempt(register), name='register'),
    url(r'^edit/(?P<blog_id>\d+)', EditBlogView.as_view(), name='edit'),
    url(r'^create_blog', create_blog, name='create'),
    url(r'^show_blog/(?P<blog_id>\d+)', csrf_exempt(show_blog), name='show'),
    url(r'^save_blog/(?P<blog_id>\d+)', save_blog, name='save'),
    url(r'^pub_blog/(?P<blog_id>\d+)', pub_blog,name="publish"),
    url(r'^delete/(?P<blog_id>\d+)', delete_blog, name='delete'),
    url(r'^logout', logout, name='logout'),
    url(r'^u/(?P<user_id>\d+)', UIndexView.as_view(), name="uindex"),
]
