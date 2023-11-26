from django.shortcuts import render, redirect, HttpResponse
from .forms import ArticleForm, ModeratorForm
from django.contrib import messages
# from parser.parser import parser_vk
from AI.AI_model import exec, y, z, learn
from .models import Article
from django.views.decorators.csrf import csrf_exempt

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            print("Valid form data:", form.cleaned_data['full_text'])
            cat, theme = exec(form.cleaned_data['full_text'])
            messages.success(request, 'Ваше обращение отправлено!')
            Article(full_text=form.cleaned_data['full_text'], category=cat, theme=theme).save()
            form = ArticleForm()
            return render(request, 'circulation_page/page.html', {
                'form': form,
                'theme': theme,
                'category': cat,
            })
        else:
            error = 'Форма была неверной'
    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'circulation_page/page.html', data)


def sub(request):
    return HttpResponse('!Тестовый вывод!')


@csrf_exempt
def moderator(request):
    if request.method == 'POST':
        form = ModeratorForm(request.POST)
        # if form.is_valid():
        model = Article.objects.get(id=form.data['id'])
        if form.data['mode'] == 'ok':
            model.status = Article.Status.ACCEPTED
            model.save()
        elif form.data['mode'] == 'save':
            if form.data['category'] != '':
                model.category = form.data['category']
            if form.data['theme'] != '':
                model.theme = form.data['theme']
            learn(model.full_text, model.category, model.theme)
            model.save()
        elif form.data['mode'] == 'del':
            model.status = Article.Status.REJECTED
            model.save()


    article = Article.objects.filter(status=Article.Status.CREATED).order_by('id').first()
    if article is None:
        return render(request, 'circulation_page/moderator.html', {
            'id': None,
            'categories': z,
            'subcategories': y,
            'text': None,
            'cat': None,
            'theme': None,
        })

    return render(request, 'circulation_page/moderator.html', {
        'id': article.id,
        'categories': z,
        'subcategories': y,
        'text': article.full_text,
        'cat': article.category,
        'theme': article.theme,
    })

def submitForm(request):
    print("Test")