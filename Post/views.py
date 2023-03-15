from itertools import chain
from taggit.models import Tag
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Comment.forms import AnonymousCommentForm, UserCommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import VideoPostModel, AudioPostModel, PhotoPostModel, TextPostModel, CategoryModel
from .forms import AudioPostForm, VideoPostForm, PhotoPostForm, TextPostForm,\
    EditAudioPostForm, EditPhotoPostForm, EditTextPostForm, EditVideoPostForm


# !-------------------- Home View -----------------
def home_page_view(request):
    categories = CategoryModel.objects.all()

    if request.GET.get('Tag'):
        tag = request.GET.get('Tag')
        tag = Tag.objects.get(name=tag)
        audios = AudioPostModel.objects.filter(tags__in=[tag])
        videos = VideoPostModel.objects.filter(tags__in=[tag])
        photos = PhotoPostModel.objects.filter(tags__in=[tag])
        posts = sorted(
            chain(audios, photos, videos),
            key=lambda post: post.datetime,
            reverse=True,
        )
        return render(request, 'index.html', {'Posts': posts, 'Categories': categories})

    else:

        videos = VideoPostModel.objects.all()
        photos = PhotoPostModel.objects.all()
        audios = AudioPostModel.objects.all()
        texts = TextPostModel.objects.all()
        # videos | photos | audios | texts
        posts = sorted(
            chain(videos, photos, audios, texts),
            key=lambda post: post.datetime,
            reverse=True
        )
        last_post = [videos.last(), photos.last(), audios.last()]

        paginator = Paginator(posts, 11)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(1)

        context = {
            'Posts': posts,
            'Categories': categories,
            'Last_Post': last_post
        }
        return render(request, 'index.html', context)

#! ----------------- Detials View ---------------------


def photo_post_detail_view(request, slug):
    categories = CategoryModel.objects.all()
    post = get_object_or_404(PhotoPostModel, slug=slug)
    form = (UserCommentForm if request.user.is_authenticated else AnonymousCommentForm)
    return render(request, 'Details/single-gallery.html', {'Post': post, 'CommentForm': form, 'Categories': categories})


def audio_post_detail_view(request, slug):
    categories = CategoryModel.objects.all()
    post = get_object_or_404(AudioPostModel, slug=slug)
    form = (UserCommentForm if request.user.is_authenticated else AnonymousCommentForm)
    return render(request, 'Details/single-audio.html', {'Post': post, 'CommentForm': form, 'Categories': categories})


def video_post_detail_view(request, slug):
    categories = CategoryModel.objects.all()
    post = get_object_or_404(VideoPostModel, slug=slug)
    form = (UserCommentForm if request.user.is_authenticated else AnonymousCommentForm)

    return render(request, 'Details/single-video.html', {'Post': post, 'CommentForm': form, 'Categories': categories})

#! ----------------- Search View -----------------------


def search_view(request,):
    categories = CategoryModel.objects.all()
    keyword = request.GET.get("Search")

    audios = AudioPostModel.objects.filter(body__contains=keyword) | \
        AudioPostModel.objects.filter(title__contains=keyword)

    videos = VideoPostModel.objects.filter(body__contains=keyword) | \
        VideoPostModel.objects.filter(title__contains=keyword)

    photos = PhotoPostModel.objects.filter(body__contains=keyword) | \
        PhotoPostModel.objects.filter(title__contains=keyword)

    texts = TextPostModel.objects.filter(body__contains=keyword)

    posts = sorted(
        chain(audios, videos, photos, texts),
        key=lambda post: post.datetime,
        reverse=True
    )

    paginator = Paginator(posts, 11)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page_range

    return render(request, 'index.html', {'Posts': posts, 'Categories': categories})


def category_view(request, category):
    categories = CategoryModel.objects.all()
    category = CategoryModel.objects.get(name=category)

    audios = AudioPostModel.objects.filter(category=category)

    videos = VideoPostModel.objects.filter(category=category)

    photos = PhotoPostModel.objects.filter(category=category)

    posts = sorted(
        chain(audios, photos, videos),
        key=lambda post: post.datetime,
        reverse=True
    )

    paginator = Paginator(posts, 11)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(1)

    return render(request, 'index.html', {'Category': category, 'Posts': posts, 'Categories': categories, 'page': page})


#!---------- New Post Views -----------
def select_view(request):
    return render(request, 'Create/select.html')


@login_required(login_url='Accounts:login')
def new_audio_post_view(request):
    categories = CategoryModel.objects.all()

    if request.method == 'POST':
        form = AudioPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = AudioPostModel()
            cd = form.cleaned_data
            post.title = cd['title']
            post.body = cd['body']
            post.author = request.user
            post.audio = cd['audio']
            post.cover = cd['cover']
            post.slug = cd['slug']
            post.save()

            for category in cd['category']:
                post.category.add(category.id)

            tags = cd['tags']
            for tag in tags:
                tag = tag.strip()
                post.tags.add(tag)
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = AudioPostForm()
    return render(request, 'Create/audio_post.html', {'form': form, 'Categories': categories})


@login_required(login_url='Accounts:login')
def new_video_post_view(request):
    categories = CategoryModel.objects.all()

    if request.method == 'POST':
        form = VideoPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = VideoPostModel()
            cd = form.cleaned_data
            post.title = cd['title']
            post.body = cd['body']
            post.author = request.user
            post.video = cd['video']
            post.cover = cd['cover']
            post.slug = cd['slug']
            post.save()

            for category in cd['category']:
                post.category.add(category.id)

            tags = cd['tags']
            for tag in tags:
                tag = tag.strip()
                post.tags.add(tag)
            post.save()
            return redirect(post.get_absolute_url())
        else:
            form = VideoPostForm()
    else:
        form = VideoPostForm()
    return render(request, 'Create/video_post.html', {'form': form, 'Categories': categories})


@login_required(login_url='Accounts:login')
def new_photo_post_view(request):
    categories = CategoryModel.objects.all()

    if request.method == 'POST':
        form = PhotoPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = PhotoPostModel()
            cd = form.cleaned_data
            post.title = cd['title']
            post.body = cd['body']
            post.author = request.user
            post.image = cd['image']
            post.slug = cd['slug']
            post.save()

            for category in cd['category']:
                post.category.add(category.id)

            tags = cd['tags']
            for tag in tags:
                tag = tag.strip()
                post.tags.add(tag)
            post.save()
            return redirect(post.get_absolute_url())
        else:
            form = PhotoPostForm()
    else:
        form = PhotoPostForm()
    return render(request, 'Create/photo_post.html', {'form': form, 'Categories': categories})


@login_required(login_url='Accounts:login')
def new_text_post_view(request):

    if request.method == 'POST':
        form = TextPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = TextPostModel()
            cd = form.cleaned_data
            post.body = cd['body']
            post.author = request.user
            post.save()
            return redirect('Post:Home')
        else:
            form = TextPostForm()
    else:
        form = TextPostForm()
    return render(request, 'Create/text_post.html', {'form': form, })


# ! -------------- Edit Post Views ---------------
@login_required(login_url='Accounts:login')
def edit_audio_post_view(request, post_id):
    categories = CategoryModel.objects.all()

    post = AudioPostModel.objects.get(id=post_id)
    if post.author == request.user:
        if request.method == 'POST':
            form = EditAudioPostForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                post.title = cd['title']
                post.body = cd['body']
                if cd['audio'] is not None:
                    post._delete_file_(audio=True)
                    post.audio = cd['audio']

                if cd['cover'] is not None:
                    post._delete_file_(cover=True)
                    post.cover = cd['cover']

                if not cd['slug'] == post.slug:
                    post.slug = cd['slug']

                post.category.clear()
                for category in cd['category']:
                    post.category.add(category.id)

                post.tags.clear()
                tags = cd['tags']
                tags = tags.split(',')
                for tag in tags:
                    tag = tag.strip()
                    post.tags.add(tag)

                post.save()

                return redirect(post.get_absolute_url())
        else:
            form = EditAudioPostForm()
    else:
        return HttpResponse('403')
    return render(request, "Create/audio_post.html", {'form': form, 'Post': post, 'Categories': categories})


@login_required(login_url='Accounts:login')
def edit_video_post_view(request, post_id):
    categories = CategoryModel.objects.all()

    post = VideoPostModel.objects.get(id=post_id)
    if post.author == request.user:
        if request.method == 'POST':
            form = EditVideoPostForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                post.title = cd['title']
                post.body = cd['body']
                if cd['video'] is not None:
                    post._delete_file_(video=True)
                    post.video = cd['video']

                if cd['cover'] is not None:
                    post._delete_file_(cover=True)
                    post.cover = cd['cover']

                if not cd['slug'] == post.slug:
                    post.slug = cd['slug']

                post.category.clear()
                for category in cd['category']:
                    post.category.add(category.id)

                post.tags.clear()
                tags = cd['tags']
                tags = tags.split(',')
                for tag in tags:
                    tag = tag.strip()
                    post.tags.add(tag)

                post.save()

                return redirect(post.get_absolute_url())
        else:
            form = EditVideoPostForm()
    else:
        return HttpResponse('403')
    return render(request, "Create/video_post.html", {'form': form, 'Post': post, 'Categories': categories})


@login_required(login_url='Accounts:login')
def edit_photo_post_view(request, post_id):
    categories = CategoryModel.objects.all()

    post = PhotoPostModel.objects.get(id=post_id)
    if post.author == request.user:
        if request.method == 'POST':
            form = EditPhotoPostForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                post.title = cd['title']
                post.body = cd['body']
                if cd['image'] is not None:
                    post._delete_file_()
                    post.image = cd['image']

                if not cd['slug'] == post.slug:
                    post.slug = cd['slug']

                post.category.clear()
                for category in cd['category']:
                    post.category.add(category.id)

                post.tags.clear()
                tags = cd['tags']
                tags = tags.split(',')
                for tag in tags:
                    tag = tag.strip()
                    post.tags.add(tag)

                post.save()

                return redirect(post.get_absolute_url())
        else:
            form = EditPhotoPostForm()
    else:
        return HttpResponse('403')
    return render(request, "Create/photo_post.html", {'form': form, 'Post': post, 'Categories': categories})


@login_required(login_url='Accounts:login')
def edit_text_post_view(request, post_id):
    categories = CategoryModel.objects.all()

    post = TextPostModel.objects.get(id=post_id)
    if request.user == post.author:
        if request.method == 'POST':
            form = EditTextPostForm(request.POST)
            if form.is_valid():
                post.body = form.cleaned_data['body']
                post.save()
                return redirect('Post:Home')
        else:
            form = EditTextPostForm()
    else:
        return HttpResponse('403')
    return render(request, "Create/text_post.html", {'form': form, 'Post': post, 'Categories': categories})


# ! ------------- Delete Post Views --------------

@login_required(login_url='Accounts:login')
def delete_audio_post_view(request, pk):
    audio = AudioPostModel.objects.get(id=pk)
    if request.user == audio.author:
        if request.method == 'POST':
            audio._delete_file_(cover=True, audio=True)
            audio.delete()
            return redirect('Post:Home')
        else:
            pass
    else:
        return HttpResponse('<h1 style="color:red">403</h1>')

    return render(request, 'delete.html')


@login_required(login_url='Accounts:login')
def delete_video_post_view(request, pk):
    video = VideoPostModel.objects.get(id=pk)
    if request.user == video.author:
        if request.method == 'POST':
            video._delete_file_(cover=True, video=True)
            video.delete()
            return redirect('Post:Home')
        else:
            pass
    else:
        return HttpResponse('<h1 style="color:red">403</h1>')

    return render(request, 'delete.html')


@login_required(login_url='Accounts:login')
def delete_photo_post_view(request, pk):
    photo = PhotoPostModel.objects.get(id=pk)
    if request.user == photo.author:
        if request.method == 'POST':
            photo._delete_file_()
            photo.delete()
            return redirect('Post:Home')
        else:
            pass
    else:
        return HttpResponse('<h1 style="color:red">403</h1>')

    return render(request, 'delete.html')


@login_required(login_url='Accounts:login')
def delete_text_post_view(request, pk):
    text = TextPostModel.objects.get(id=pk)
    if request.user == text.author:
        if request.method == 'POST':
            text.delete()
            return redirect('Post:Home')
        else:
            pass
    else:
        return HttpResponse('<h1 style="color:red">403</h1>')

    return render(request, 'delete.html')
