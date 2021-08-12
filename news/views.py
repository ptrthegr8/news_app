from django.shortcuts import render
from news.models import Article, Author

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
