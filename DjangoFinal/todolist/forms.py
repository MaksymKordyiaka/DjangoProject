from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority', 'completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Назва завдання',
            'due_date': 'Дедлайн',
            'priority': 'Пріоритет',
            'completed': 'Виконано',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Визначення, чи форма використовується для редагування існуючого завдання
        is_editing = self.instance.pk is not None

        # Якщо форма використовується для створення нового завдання
        if not is_editing:
            # Встановлення атрибуту readonly для поля completed, щоб воно було видимим, але не редагованим
            self.fields['completed'].widget.attrs['readonly'] = True