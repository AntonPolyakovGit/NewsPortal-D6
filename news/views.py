from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Post, Author


class AuthorList(ListView):
    model = Author
    context_object_name = 'Author'

class PostsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'












