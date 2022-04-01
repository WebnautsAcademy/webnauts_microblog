from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'gallery/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'gallery/post_detail.html', {'object': post})


def create_post(request):
    form = PostForm
    if request.method == 'GET':
        return render(request, 'gallery/post_form.html', {'form': form})
    data = PostForm(request.POST, request.FILES)
    if data.is_valid():
        post = data.save(commit=False)
        post.user = request.user
        post.save()
    return redirect('post_list')


class PostList(ListView):
    model = Post
    # paginate_by = 2


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ('title', 'file', 'description')
    success_url = '/gallery/'


class PostUpdate(UpdateView):
    model = Post
    fields = ('title', 'file', 'description')
    template_name_suffix = "_update_form"
    success_url = '/gallery/'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
