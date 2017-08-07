from django.views.generic import ListView, DetailView

from blog.models import Blog


class IndexView(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        blogs = Blog.objects.filter(status='P')
        return blogs

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
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