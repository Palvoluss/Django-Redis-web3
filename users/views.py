from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.views import Post 


def register(request):

    context = { }

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username  = form.cleaned_data.get("username")
            messages.success(request, f"Your account has benne created! You are now able to log in")
            form.save()
            return redirect('login')
            
    else: 
        form = UserRegisterForm()
      
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)




def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author = user)

    context = {
        'user': user, 
        'posts': posts,
    }
    return render(request, 'users/user_detail.html', context)