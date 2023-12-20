from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone

def task_list(request):
    tasks = Task.objects.order_by('created_at')
    paginator = Paginator(tasks, 3)  # Кількість завдань на сторінці
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)  # Якщо 'page' не є цілим числом, відображаємо першу сторінку
    except EmptyPage:
        tasks = paginator.page(1)  # Якщо 'page' виходить за межі, відображаємо першу сторінку

    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        # Якщо форма вже була відправлена
        form = TaskForm(request.POST)
        if form.is_valid():
            # Зберігаємо завдання, встановлюючи дату створення і перенаправляємо на сторінку списку завдань
            task = form.save(commit=False)
            task.created_at = timezone.now()
            task.save()
            return redirect('task_list')
    else:
        # Якщо це GET-запит, просто відображаємо порожню форму
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)  # Використовує id як ідентифікатор
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()    # Збереження змін у формі редагування і перенаправлення на сторінку списку завдань
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)    # Отримуємо завдання за його первинним ключем або видаємо 404 помилку, якщо не знайдено
    task.delete()  # Видалення завдання з бази даних
    return redirect('task_list')  # Перенаправлення на сторінку списку завдань після видалення