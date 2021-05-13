from django.db import models

# Create your models here.


class AnimePost(models.Model):
    title   = models.CharField(max_length=120)
    address =  models.CharField(max_length=200, null=True)
    content = models.TextField()
    cv = models.TextField(default='')
    profile_pic = models.ImageField(null=False, upload_to='Anime_img')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Post from {} created at {}".format(self.title, self.created)

    class Meta:
        pass
    
    def get_absolute_url(self):
        return '/list/'

class CartoonPost(models.Model):
    title   = models.CharField(max_length=120)
    address =  models.CharField(max_length=200, null=True)
    content = models.TextField()
    profile_pic = models.ImageField(null=True, upload_to='cartoon_img')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Post from {} created at {}".format(self.title, self.created)

    class Meta:
        pass
    
    def get_absolute_url(self):
        return '/cartoon/'


        
class SingerPost(models.Model):
    sing_name   = models.CharField(max_length=120)
    address =  models.CharField(max_length=200, null=True)
    content = models.TextField()
    profile_pic = models.ImageField(null=True, upload_to='singer_img')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sing_Born = models.CharField(max_length=50,default='')
    sing_Genres = models.CharField(max_length=50,default='')
    sing_career = models.TextField(default='')

    def __str__(self):
        return "Post from {} created at {}".format(self.sing_name, self.created)

    class Meta:
        pass
    
    def get_absolute_url(self):
        return '/singer/'



class BlogPostDetail(models.Model):
    title   = models.CharField(max_length=120)
    author_name =  models.CharField(max_length=100, null=True,default='')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Post from {} created at {}".format(self.title, self.created)

    class Meta:
        pass
    
    def get_absolute_url(self):
        return '/blog/'


        