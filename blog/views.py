from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post

def post_list(request):
    latest_post_list = Post.objects.order_by('published_date')
    template = loader.get_template('blog/post_list.html')
    context = {'latest_post_list': latest_post_list}
    return HttpResponse(template.render(context, request))

def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
            raise Http404('Il post che stai cercando non esiste')
    return render(request, 'blog/post_detail.html', { 'post': post})