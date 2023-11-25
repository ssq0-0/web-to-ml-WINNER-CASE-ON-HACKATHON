from django.shortcuts import render, redirect, HttpResponse
from .forms import ArticleForm, Moder
from django.contrib import messages
# from parser.parser import parser_vk
from AI.AI_model import run


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            print("Valid form data:", form.cleaned_data)
            # Отправка данных в задачу Celery
            # ai_process_task.delay(form.cleaned_data)
            # Переадресация на страницу, которая будет показывать статус обработки/пока что переадресация на ту же страницу
            messages.success(request, 'Ваше обращение отправлено!')
            return redirect('home')
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


def moderator(request):
    items = Moder.objects.all()
    #  здесь вызов функции парсинга и передача ему текста с формы
    return render(request, 'circulation_page/moderator.html', {'items': items})