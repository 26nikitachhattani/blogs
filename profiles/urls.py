from django.contrib import admin
from django.urls import path
from .views import ProfileListView, ProfileDetailView, follow_unfollow_profile

app_name = 'profile'

urlpatterns = [
    path('',ProfileListView.as_view(), name='profile-list-view'),
    path('switch-follow/',follow_unfollow_profile, name='follow-unfollow-view'),
    path('<pk>',ProfileDetailView.as_view(), name='profile-detail-view'),
]