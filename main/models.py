from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_content = models.CharField(max_length=400)
    post_date = models.DateTimeField(auto_now_add=True)
    post_likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)

    def __str__(self):
        return '%s - %s - %s' % (self.post_content, self.post_date, self.post_likes)

    class Meta:
        ordering = ['-post_date']

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=100)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.comment_post, self.comment_user)

class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/')
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_name = models.CharField(max_length=100)
    profile_bio = models.CharField(max_length=300)
    profile_followers = models.ManyToManyField(User, related_name='followers', blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.profile_name, self.profile_bio)

