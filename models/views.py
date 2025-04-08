from .models import Model
from django.views.generic import ListView, DetailView


class ModelList(ListView):
   #paginate_by = 12
    model = Model
    template_name = 'models/model_list.html'
    queryset = Model.objects.all()


class ModelDetail(DetailView):
    model = Model
    template_name = 'models/model_detail.html'
    queryset = Model.objects.all()