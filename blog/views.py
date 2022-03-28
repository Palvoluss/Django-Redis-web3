from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post
import redis

SERVER_IP = '127.0.0.1'
SERVER_PORT = '6379'
PASSWORD = ''
DB = 0


def home_layout(request):
    return render(request, 'home/home_layout.html')

def home_post_list(request):

    diffIP = False
    user_email = request.user.email
    client = redis.StrictRedis(host=SERVER_IP, 
                                port=SERVER_PORT, 
                                password=PASSWORD,
                                db=DB,
                                charset="utf-8", 
                                decode_responses=True)

    last_ip = client.get(user_email)
    current_ip = request.META['REMOTE_ADDR']

    if current_ip != last_ip:
        client.set(user_email, current_ip)
        if current_ip != None: 
            diffIP = True

    return render(request, 'home/home_post_list.html')

def home_category_list(request):
    return render(request, 'home/home_category_list.html')

def post_list(request):
    latest_post_list = Post.objects.order_by('published_date')
    template = loader.get_template('blog/post_list.html')
    context = {'latest_post_list': latest_post_list}
    return HttpResponse(template.render(context, request))

def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        category = post.category.all()
        context = {
             'post': post,
             'category': category
        }
    except Post.DoesNotExist:
            raise Http404('Il post che stai cercando non esiste')
    return render(request, 'blog/post_detail.html', context)
    