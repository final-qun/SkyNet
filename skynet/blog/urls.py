from django.conf.urls import url
from blog.views import *


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^detail/(?P<post_id>\d+)$',PostDetailView.as_view(), name='detail'),
    url(r'^login/', login, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^edit/',EditPostView.as_view(), name='edit'),
    url(r'^add_new_post',csrf_exempt(add_new_post),name='add_new_post'),
    url(r'^show_post/(?P<post_id>\d+)',csrf_exempt(show_post),name='show_post'),
    url(r'^save_post/(?P<post_id>\d+)',csrf_exempt(save_post),name='save_post')
]