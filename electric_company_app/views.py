from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'electric_company_app/home.html')

def oferta(request):
    return render(request, 'electric_company_app/oferta.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'electric_company_app/post_list.html', {'posts':posts})

def new_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(post_list)

    return render(request, 'electric_company_app/post_form.html', {'form': form})

def edit_post(request, id):
    post2 = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, request.FILES or None,
                    instance=post2)

    if form.is_valid():
        form.save()
        return redirect(post_list)

    return render(request, 'electric_company_app/post_form.html', {'form': form})




