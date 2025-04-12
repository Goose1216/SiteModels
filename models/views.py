from .models import Model, Like, Comment
from django.http import HttpResponseNotAllowed
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect


class ModelList(ListView):
   #paginate_by = 12
    model = Model
    template_name = 'models/model_list.html'
    queryset = Model.objects.all()


class ModelDetail(DetailView):
    model = Model
    template_name = 'models/model_detail.html'
    queryset = Model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.get_object()
        user = self.request.user

        context['liked'] = False
        context['commented'] = False
        if user.is_authenticated:
            context['liked'] = Like.objects.filter(model=model, author=user).exists()
            context['commented'] = Comment.objects.filter(model=model, author=user).exists()

        return context

def increment_downloads(request, pk):
    if request.method == "POST":
        model = get_object_or_404(Model, id=pk)
        model.increment_downloads()
        return redirect('models_detail', pk=pk)
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def add_like(request, pk):
    model = get_object_or_404(Model, id=pk)

    if request.method == "POST":
        Like.objects.get_or_create(model=model, author=request.user)

    return redirect('models_detail', pk=pk)

@login_required
def delete_like(request, pk):
    model = get_object_or_404(Model, id=pk)

    if request.method == "POST":
        try:
            like = Like.objects.get(model=model, author=request.user)
            like.delete()
        except Like.DoesNotExist:
            pass

    return redirect('models_detail', pk=pk)

@login_required
def toggle_comment(request, pk):
    model = get_object_or_404(Model, id=pk)

    if request.method == "POST":
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(model=model, author=request.user, comment=comment_text)
    return redirect('models_detail', pk=pk)