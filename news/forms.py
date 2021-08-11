from django import forms
from news.models import Author

"""
create an article

title = models.CharField(max_length=50)
body = models.TextField()
post_created = models.DateTimeField(default=timezone.now)
author = models.ForeignKey(Author, on_delete=models.CASCADE)

create an author

name = models.CharField(max_length=50)
byline = models.CharField(max_length=50, null=True, blank=True)
"""


class AddArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "byline"]
