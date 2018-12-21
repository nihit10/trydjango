from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_list=Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts_list, 5) # Show 25 contacts per page
    #page_request_var="abc"
    #page = request.GET.get('page_request_var)
    page = request.GET.get('page')
    posteed = paginator.get_page(page)
    return render(request, 'index.html', {'posteed': posteed})



    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES or None, instance=post) #diff instance=post for edit 
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts:post_list')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user =authenticate(username=username,
                password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return  HttpResponseRedirect(reverse('posts:post_list'))
                else:
                    return HttpResponse('User is not active')
            else:
                return HttpResponse('User is None')
    else:
        form=UserLoginForm()

    context={
        'form': form,
     }
    return render(request,'login.html',context)

def user_logout(request):
    logout(request)
    return redirect('posts:post_list')
