from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CommentForm, PostForm, ProfileForm
from .models import Post, Comment, Profile
from django.http import HttpResponseRedirect
from django.urls import reverse


def homepage(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    comment_form = CommentForm(request.POST)
    post_form = PostForm(request.POST)

    if post_form.is_valid():
        instance = post_form.save(commit=False)
        instance.post_user = request.user
        instance.save()
        return redirect('/')

    for post in posts:
        print(post.post_likes.count())

    return render(request, 'main/home.html', {'posts': posts, 'form':comment_form, 'post_form':post_form})


def searchView(request):
    profile = Profile.objects.filter(profile_user=request.user)
    if request.method == 'GET':
        search_query = request.GET.get('search_user', None)
        q = User.objects.filter(username__contains=search_query)
        return render(request, 'main/results.html', {'users':q, 'profiles':profile})
    else:
        print('search did not work!')


def commentView(request, pk):
    form = CommentForm(request.POST)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.comment_user = request.user
        instance.comment_post = get_object_or_404(Post, pk=pk)
        instance.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def otherProfileView(request, pk):
    post_user = get_object_or_404(User, pk=pk)
    user_profile = Profile.objects.filter(profile_user=pk)
    user_posts = Post.objects.filter(post_user=pk)
    user_comments = Comment.objects.filter(comment_user=pk)
    print(user_posts)
    return render(request, 'main/other_profile.html', {'user':post_user, 'profile':user_profile, 'posts':user_posts, 'comments':user_comments})


def followView(request, pk):
    user = request.user
    follower_user = get_object_or_404(Profile, pk=pk)
    print(follower_user)

    if user in follower_user.profile_followers.all():
        follower_user.profile_followers.remove(user)
        print('unfollowed')

    else:
        follower_user.profile_followers.add(user)
        print('followed')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def profileEdit(request, pk):
    form = ProfileForm(request.POST, request.FILES)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.profile_user = request.user
        instance.save()
        return redirect('/')
    return render(request, 'main/profile_edit.html', {'form':form})


def registerView(request):
    form = UserCreationForm(request.POST)

    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        login(request, user)
        return redirect('/')
    return render(request, 'main/register.html', {'form':form})


def loginView(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            print('form is valid')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            print('not valid')
            print(form.errors)

    return render(request, 'main/login.html', {'form':form})


def logoutView(request):
    logout(request)
    return redirect('/')


def likeView(request, pk):
    user = request.user
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if user in post.post_likes.all():
        post.post_likes.remove(user)
        print('like removed')
    else:
        post.post_likes.add(user)
        print('liked')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deletePostView(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('/')
    else:
        print('uh oh someting went wrong')


def followingView(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    comment_form = CommentForm(request.POST)
    post_form = PostForm(request.POST)

    if post_form.is_valid():
        instance = post_form.save(commit=False)
        instance.post_user = request.user
        instance.save()
        return redirect('/')

    return render(request, 'main/following.html', {'post_form':post_form, 'form':comment_form, 'posts':posts })


def trendView(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    comment_form = CommentForm(request.POST)
    post_form = PostForm(request.POST)
    trending_posts = Post.objects.annotate(like_count=Count('post_likes')).order_by('-like_count')

    if post_form.is_valid():
        instance = post_form.save(commit=False)
        instance.post_user = request.user
        instance.save()
        return redirect('/')

    return render(request, 'main/trending.html', {'posts':trending_posts, 'post_form':post_form})

