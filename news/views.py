from django.shortcuts import render, HttpResponseRedirect, reverse
from news.models import Article, Author
from news.forms import AddArticleForm, AddAuthorForm

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


def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("home"))
    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})
