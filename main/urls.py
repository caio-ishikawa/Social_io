from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
        path('', views.homepage, name='homepage'),
        path('register/', views.registerView, name='register'),
        path('login/', views.loginView, name='login'),
        path('like/<int:pk>/', views.likeView, name='like'),
        path('logout/', views.logoutView, name='logout'),
        path('comment/<int:pk>/', views.commentView, name='comment'),
        path('profile/edit/<int:pk>/', views.profileEdit, name='profile_edit'),
        path('profile/p/<int:pk>/', views.otherProfileView, name='other_profile'),
        path('post/delete/<int:pk>/', views.deletePostView, name='delete_post'),
        path('search/', views.searchView, name='results'),
        path('profile/follow/<int:pk>/', views.followView, name='follow'),
        path('feed/following/', views.followingView, name='following'),
        path('feed/trending/', views.trendView, name='trending')
]
