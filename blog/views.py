from django.views.generic import TemplateView, ListView, DetailView
from .models import Article

class BlogListView(ListView):
    model = Article
    template_name = "blog/blog_list.html"
    def get_queryset(self):
        return Article.objects.all().order_by('-created_at')


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog/blog_detail.html"
