# from django.shortcuts import render
#from pyexpat import model
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
  model = Post
  template_name = "Blog/post_list.html"
  
class PostCreateView(CreateView):
  model = Post
  fields = "__all__"
  success_url = reverse_lazy("blog:all")
  template_name = "Blog/post_form.html"
  
class PostDetailView(DetailView):
  model = Post
  template_name = "Blog/post_detail.html"
  
class PostUpdateView(UpdateView):
  model = Post
  fields = "__all__"
  success_url = reverse_lazy("blog:all")
  template_name = "Blog/post_form.html"
  
class PostDeleteView(DeleteView):
  model = Post
  fields = "__all__"
  success_url = reverse_lazy("blog:all")
  template_name = "Blog/post_confirm_delete.html"
  