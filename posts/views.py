from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_list=Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts_list, 5) # Show 25 contacts per page
    #page_request_var="abc"
    #page = request.GET.get('page_request_var)
    page = request.GET.get('page')
    posted = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posted})



    
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES or None, instance=post) #diff instance=post for edit 
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_delete(request,pk):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post_detail', slug=post.slug)