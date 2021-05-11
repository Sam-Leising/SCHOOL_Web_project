from django.contrib import admin
from .models import AnimePost, BlogPostDetail, CartoonPost, SingerPost
# Register your models here.

admin.site.register(AnimePost)
admin.site.register(BlogPostDetail)
admin.site.register(CartoonPost)
admin.site.register(SingerPost)
