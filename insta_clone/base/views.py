from django.shortcuts import render, redirect
from .models import Post

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = "posts"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["text", "image", "post_file"]
    template_name = "create_post.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect("home")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["text", "image", "post_file"]
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
