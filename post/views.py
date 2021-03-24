from django.shortcuts import render
from profiles.models import Profile
from itertools import chain

# Create your views here.
def post_of_following_profiles(request):
    # get logged in user profile
    profile = Profile.objects.get(user=request.user)
    # check who we are following
    users = [user for user in profile.following.all()]
    # initial values for variable
    post = []
    qs = None
    # get the post of the people who we are following
    for u in users:
        p = Profile.objects.get(user=u)
        p_posts = p.post_set.all()
        post.append(p_posts)
    # our posts
    my_posts = profile.profile_post()
    post.append(my_posts)
    # sort and chain querystes and unpack the post list
    if len(post)>0:
        qs = sorted(chain(*post), reverse=True, key=lambda obj:obj.created)
    return render(request, 'posts/main.html',{'post':qs})