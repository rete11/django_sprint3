from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.utils import timezone
from blog.models import Post, Category

now = timezone.now()


def index(request):
    # константа 'num_first_posts' отвечает за количество последних публикаций
    # константа 'num_offset' отвечает за сдвиг публикаций
    num_first_posts = 5
    num_offset = 0
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=now,
    ).order_by('-pub_date')[num_offset:num_first_posts]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        is_published=True,
        category__is_published=True,
        pub_date__lt=now,
        pk=pk
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_list_or_404(
        Post,
        is_published=True,
        category__is_published=True,
        pub_date__lt=now,
        category=category,
    )
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, template_name, context)
