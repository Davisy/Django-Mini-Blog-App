from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog 
# Create your views here.


class BlogListView(ListView):
    model = Blog 
    template_name = 'blog/home.html'
    ordering = ['-title']

class BlogDetailView(DetailView):
    model = Blog 
    template_name = 'blog/post_details.html'
    #you can choose the name you want to your object 
    #by write context_object_nane = 'write here the name'
    #example context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Blog 
    template_name = 'blog/post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Blog 
    fields = ['title','body']
    template_name = 'blog/post_edit.html'

class BlogDeleteView(DeleteView):
    model = Blog 
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog')
