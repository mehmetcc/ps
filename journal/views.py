from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.
def base_view(request):
    categories = Category.objects.all().order_by(Category.category_title)

    return render(request, 'base.html', {'categories': categories})


def post_list(request):
    posts = Post.objects.all().order_by('published_date').reverse()

    return render(request, 'blog_posts.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post_detail.html', {'post': post})


def categories_detail(request, slug):
    posts = Post.objects.filter(categories__slug=slug).order_by('published_date').reverse()

    return render(request, 'categories_detail.html', {'posts': posts,
                                                      'category': slug.title()})


def about(request):
    return render(request, 'about.html')

