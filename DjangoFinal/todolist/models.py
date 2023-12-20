from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)    # Явно вказане поле primary_key
    title = models.CharField(max_length=200)    # Назва завдання
    created_at = models.DateTimeField(auto_now_add=True)    # Дата та час створення завдання (автоматично встановлюється при створенні запису)
    due_date = models.DateTimeField(null=True, blank=True)    # Дедлайн
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    ], default='medium')    # Пріоритет завдання (низький, середній, високий)
    completed = models.BooleanField(default=False)    # Вказує, чи завдання виконано чи ні

    def __str__(self):    # Метод для рядкового представлення об'єкту
        return self.title

