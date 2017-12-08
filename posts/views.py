from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import RedirectView
from posts.models import Post, Comment
from posts.forms import UserForm, ProfileForm, PostForm, CommentForm
from django.db.models import Q
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='/sign-in/')
def home(request):
    return render(request, 'main.html', {})

@login_required(login_url='/sign-in/')
def post_add(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.save()
            return redirect(posts_list)
    return render(request, 'posts/add_post.html', {'form': form})

@login_required(login_url='/sign-in/')
def post_edit(request, post_id):
    form = PostForm(instance = Post.objects.get(id = post_id))
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance = Post.objects.get(id = post_id))
        if form.is_valid():
            media = form.save()
            return redirect(posts_list)
    return render(request, 'posts/edit_post.html', {'form': form})

def sign_up(request):
    user_form = UserForm()
    profile_form = ProfileForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))
            return redirect(posts_list)
    return render(request, 'posts/sign_up.html', {
        'user_form': user_form,
        'profile_form': profile_form
})

@login_required(login_url='/sign-in/')
def like(request, post_id):
    obj = get_object_or_404(Post, pk=post_id)
    user = request.user
    if user in obj.post_likes.all():
        obj.post_likes.remove(user)
    else:
        obj.post_likes.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

@login_required(login_url='/sign-in/')
def posts_list(request):
    posts_list = Post.objects.all().order_by('-id')

    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
                Q(post_title__icontains=query) |
                Q(post_city__icontains=query) |
                Q(post_country__icontains=query) |
                Q(post_content__icontains=query)
                ).distinct()
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')
    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_pages)
    return render(request, 'posts/posts_list.html', {'posts_list': posts_list,})

@login_required(login_url='/sto/sign-in/')
def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'posts/details.html', {'post': post})

@login_required(login_url='/sto/sign-in/')
def add_comment_to_post(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post = post
            print('post: ' + str(post))
            comment.comment_author = request.user
            comment.save()
            return redirect('post-detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'posts/add_comment.html', {'form': form})
