from django import forms
from .models import Post, Category, Comment

# choices = [('testing', 'testing'), ('cricket', 'cricket'), ('sports', 'sports'), ]

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'header_image', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title Here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title Tag Here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog Content Here'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Article Snippet Here (this will appear on home page)'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title Here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title Tag Here'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog Content Here'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Article Snippet here(this will appear on home page)'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name Here...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment here...'}),
        }
