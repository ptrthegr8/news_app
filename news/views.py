from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from news.models import Article, Author
from news.forms import AddArticleForm, AddAuthorForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


# Create your views here.
def index_view(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, "article_detail.html", {"article": article})


def author_detail(request, id):
    author = Author.objects.get(id=id)
    articles = Article.objects.filter(author=author)
    return render(
        request, "author_detail.html", {"author": author, "articles": articles}
    )


@login_required
def add_article(request):
    if request.method == "POST":
        form = AddArticleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            article = Article.objects.create(
                title=data["title"], body=data["body"], author=data["author"]
            )
            return HttpResponseRedirect(reverse("home"))
    form = AddArticleForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data["username"], password=data["password"]
            )
            Author.objects.create(
                name=data["name"], byline=data["byline"], user=user
            )
        return HttpResponseRedirect(reverse("home"))
    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            foo = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if foo:
                login(request, foo)
                return HttpResponseRedirect(request.GET.get("next", reverse("home")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})
