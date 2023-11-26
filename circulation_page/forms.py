from django.forms import ModelForm, TextInput, Textarea, Form, CharField
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['full_text']

        widgets = {
                'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите обращение'
            }),
        }

class ModeratorForm(Form):
    id = CharField(label="id", max_length=100)
    theme = CharField(label="theme", max_length=100)
    category = CharField(label="category", max_length=100)
    mode = CharField(label="mode", max_length=100)
