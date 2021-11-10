from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Post
from .forms import PostForm
import reversion
from reversion.views import create_revision

from .helper import render_html

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "website/home.html", {"posts": posts})

@create_revision()
def create(request, post_title = None):


    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            reversion.set_comment("created new post")

            return redirect("home")
    else:
        form = PostForm()

    return render(request, "website/create.html", {"form": form})

@create_revision()
def edit(request, post_title):


    posts = Post.objects.all()
    post = posts.get(title = post_title)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():

            if form.has_changed():
                form.save()
                reversion.set_comment("changed content/title")

            return redirect("view", post_title = post.title)
    else:
        form = PostForm(initial={"title":post.title,"content":post.content})

    return render(request, "website/edit.html", {"form": form, "post": post})

@create_revision()
def delete(request, post_title):
    Post.objects.get(title = post_title).delete()

    return redirect("home")

def view(request, post_title):

    try:
        post = Post.objects.get(title = post_title)
    except ObjectDoesNotExist:
        return redirect("create", post_title = post_title)

    post.content = render_html(post.content)

    return render(request, "website/content.html", {"post": post})
