from .models import Model, Like, Comment
from django.http import HttpResponseNotAllowed
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .forms import ModelForm

class ModelUploadView(LoginRequiredMixin, CreateView):
    model = Model
    form_class = ModelForm
    template_name = 'models/model_upload.html'
    success_url = reverse_lazy('models_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ModelPopularList(ListView):
    model = Model
    template_name = 'main.html'
    queryset = Model.objects.annotate(
        likes_count=Count('likes')
    ).order_by("-likes_count")


class ModelList(ListView):
    paginate_by = 9
    model = Model
    template_name = 'models/model_list.html'

    def get_queryset(self):
        author = self.request.GET.get('author')
        if author is None:
            return Model.objects.all()
        if author:
            return Model.objects.filter(author__username=author).select_related('author')

    def get_context_data(self, **kwargs):
        author = self.request.GET.get('author')
        context = super().get_context_data(**kwargs)

        if author is None:
            return context

        context['author'] = author
        return context


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