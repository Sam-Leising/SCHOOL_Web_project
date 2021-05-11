from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import AnimePost
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import BlogPostDetail, CartoonPost, SingerPost



class ViewAnimePost(ListView):
        queryset = AnimePost.objects.all()
        template_name = 'anime.html'

class CreateAnimePost(LoginRequiredMixin, CreateView):
        login_url = '/login/'
        model = AnimePost
        fields = '__all__'
        template_name = 'AnimePost_create_form.html'

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('anime'))
                
class UpdateAnimePost(UpdateView):
        model = AnimePost
        fields = ['title', 'address', 'content','cv','profile_pic']
        template_name = 'AnimePost_update_form.html'

        def get_object(self, queryset=None):
                id = self.kwargs['id']
                return self.model.objects.get(id=id)

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('anime'))

class DeleteAnimePost(DeleteView):
        model = AnimePost
        template_name = 'AnimePost_delete_form.html'

        def get_success_url(self):
                return reverse('anime')

#----------------------cartoon----------------------------
class ViewCartoonPost(ListView):
        queryset = CartoonPost.objects.all()
        template_name = 'cartoon.html'

class CreateCartoonPost(LoginRequiredMixin, CreateView):
        login_url = '/login/'
        model = CartoonPost
        fields = '__all__'
        template_name = 'CartoonPost_create_form.html'

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('cartoon'))
                
class UpdateCartoonPost(UpdateView):
        model = CartoonPost
        fields = ['title', 'address', 'content','profile_pic']
        template_name = 'CartoonPost_update_form.html'

        def get_object(self, queryset=None):
                id = self.kwargs['id']
                return self.model.objects.get(id=id)

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('cartoon'))

class DeleteCartoonPost(DeleteView):
        model = CartoonPost
        template_name = 'CartoonPost_delete_form.html'

        def get_success_url(self):
                return reverse('cartoon')


#----------------------singer----------------------------
class ViewSingerPost(ListView):
        queryset = SingerPost.objects.all()
        template_name = 'singer.html'

class ViewSingerdetailPost(ListView):
        queryset = SingerPost.objects.all()
        template_name = 'singer_about.html'

class CreateSingerPost(LoginRequiredMixin, CreateView):
        login_url = '/login/'
        model = SingerPost
        fields = '__all__'
        template_name = 'SingerPost_create_form.html'

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('singer'))
                
class UpdateSingerPost(UpdateView):
        model = SingerPost
        fields = ['sing_name','sing_Born', 'sing_Genres','sing_career','address', 'content','profile_pic']
        template_name = 'SingerPost_update_form.html'

        def get_object(self, queryset=None):
                id = self.kwargs['id']
                return self.model.objects.get(id=id)

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('singer'))

class DeleteSingerPost(DeleteView):
        model = SingerPost
        template_name = 'SingerPost_delete_form.html'

        def get_success_url(self):
                return reverse('singer')



#-----------------------blog-----------------------------
class ViewBlogPost(ListView):
        queryset = BlogPostDetail.objects.all()
        template_name = 'blog.html'


class CreateBlogPost(LoginRequiredMixin, CreateView):
        login_url = '/login/'
        model = BlogPostDetail
        fields = '__all__'
        template_name = 'Blog_create.html'

        def form_valid(self, form):
                model = form.save(commit=False)
                model.save()
                return HttpResponseRedirect(reverse('blog'))

class DeleteBlogPost(DeleteView):
        model = BlogPostDetail
        template_name = 'Blog_delete.html'

        def get_success_url(self):
                return reverse('blog')

                