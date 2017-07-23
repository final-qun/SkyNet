from django.conf.urls import url
from blog.views import *


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^detail/(?P<post_id>\d+)$',PostDetailView.as_view(), name='detail'),

    url(r'^login/', csrf_exempt(login), name='login'),
    url(r'^register/', csrf_exempt(register), name='register'),

    url(r'^edit/(?P<blog_id>\d+)',EditPostView.as_view(), name='edit'),
    url(r'^create_blog',create_blog,name='create_blog'),
    url(r'^show_blog/(?P<post_id>\d+)',csrf_exempt(show_post),name='show_post'),
    url(r'^save_blog/(?P<blog_id>\d+)',save_blog,name='save_blog'),
    url(r'^logout',logout,name='logout'),
    url(r'^u/(?P<user_id>\d+)',UIndexView.as_view(),name="uindex"),
]