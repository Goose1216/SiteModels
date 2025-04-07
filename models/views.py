from django.shortcuts import render
from .models import Model  # Импортируем вашу модель Model


def model_list(request):
    """
    View для отображения списка всех 3D-моделей.
    """
    # Получаем все модели из базы данных
    models = Model.objects.all()

    # Передаем их в контекст шаблона
    context = {
        'models': models,
    }

    # Рендерим шаблон с контекстом
    return render(request, 'models/model_list.html', context)