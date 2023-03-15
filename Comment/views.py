from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import UserCommentForm , AnonymousCommentForm
from Post.models import AudioPostModel , PhotoPostModel , VideoPostModel
from .models import PhotoPostCommentModel , AudioPostCommentModel , VideoPostCommentModel

def add_audio_post_comment(request,slug):
    
    post = AudioPostModel.objects.get(slug=slug)
    
    if request.method == 'POST': 
        if request.user.is_authenticated: # !logined User comment
            form = UserCommentForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                comment = AudioPostCommentModel()
                user = request.user
                comment.name = (
                    f'{user.first_name} {user.last_name}'
                    if user.first_name or user.last_name
                    else user.username)
                comment.email = user.email
                comment.message = cd['message']
                comment.website = 'ex.com'
                comment.user = user
                comment.post = post
                comment.save()
                
                return redirect(post.get_absolute_url())
            else:
                pass
    else: # !Anonymous User comment 
        form = AnonymousCommentForm(request.POST)
        if form.is_valid():
            comment = AudioPostCommentModel()
            cd = form.cleaned_data
            comment.name = cd['name']
            comment.email = cd['email']
            comment.website = cd['website']
            comment.message = cd['message']
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            pass
    return HttpResponse('404')
    
def add_video_post_comment(request,slug):
    
    post = VideoPostModel.objects.get(slug=slug)
    
    if request.method == 'POST':
        if request.user.is_authenticated: # !logined User comment 
            form = UserCommentForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                comment = VideoPostCommentModel()
                user = request.user
                comment.name = (
                    f'{user.first_name} {user.last_name}'
                    if user.first_name or user.last_name
                    else user.username)
                comment.email = user.email
                comment.message = cd['message']
                comment.website = 'ex.com'
                comment.user = user
                comment.post = post
                comment.save()
                
                return redirect(post.get_absolute_url())
            else:
                pass
    else: # !Anonymous User comment form
        form = AnonymousCommentForm(request.POST)
        if form.is_valid():
            comment = VideoPostCommentModel()
            cd = form.cleaned_data
            comment.name = cd['name']
            comment.email = cd['email']
            comment.website = cd['website']
            comment.message = cd['message']
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            pass
    return HttpResponse('404')

def add_photo_post_comment(request,slug):
    
    post = PhotoPostModel.objects.get(slug=slug)
    
    if request.method == 'POST':
        if request.user.is_authenticated: # !logined User comment form
            form = UserCommentForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                comment = PhotoPostCommentModel()
                user = request.user
                comment.name = (
                    f'{user.first_name} {user.last_name}'
                    if user.first_name or user.last_name
                    else user.username)
                comment.email = user.email
                comment.message = cd['message']
                comment.website = 'ex.com'
                comment.user = user
                comment.post = post
                comment.save()
                
                return redirect(post.get_absolute_url())
            else:
                pass
    else: # !Anonymous User comment form
        form = AnonymousCommentForm(request.POST)
        if form.is_valid():
            comment = PhotoPostCommentModel()
            cd = form.cleaned_data
            comment.name = cd['name']
            comment.email = cd['email']
            comment.website = cd['website']
            comment.message = cd['message']
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            pass
    return HttpResponse('404')



