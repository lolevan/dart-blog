from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.db.models import F

from blog.models import *


class PostsByCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = False
    # return render(request, 'blog/category.html')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context

    # def get_queryset(self):
    #     return


class PostsByTag(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsByTag, self).get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])


class GetPost(DeleteView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GetPost, self).get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(Post, self).get_context_data(**kwargs)
    #     context['title'] = self.kwargs['slug']


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))
