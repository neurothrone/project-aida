from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.views import View
from django.urls import reverse_lazy

from apps.aida.models.health.heart import Heart


class List(generic.ListView):
    model = Heart
    context_object_name = "hearts"
    queryset = Heart.find_all()
    template_name = "aida/health/heart/list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context["title"] = "Heart metrics data"
        return context


class Create(generic.CreateView):
    model = Heart
    context_object_name = "heart"
    template_name = "aida/generic/form.html"
    fields = ("measured_at", "systolic", "diastolic", "pulse")
    success_url = reverse_lazy("aida:heart-list")

    def form_valid(self, form):
        messages.success(self.request, "Heart data created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to create Heart data.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context["action"] = "Create"
        return context


class Detail(generic.DetailView):
    model = Heart
    context_object_name = "heart"
    template_name = "aida/health/heart/detail.html"


class Update(generic.UpdateView):
    model = Heart
    context_object_name = "heart"
    template_name = "aida/generic/form.html"
    fields = ("measured_at", "systolic", "diastolic", "pulse")
    success_url = reverse_lazy("aida:heart-list")

    def form_valid(self, form):
        messages.success(self.request, "Heart data updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update Heart data.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context["action"] = "Update"
        return context


class Delete(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponse:
        heart = Heart.find_by_id(pk)
        context = {
            "object": heart,
            "type": "heart",
        }
        return render(request, "aida/generic/delete.html", context)

    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        heart = Heart.find_by_id(pk)
        if heart:
            heart.delete()
            messages.success(request, "Heart data deleted.")
            return redirect("aida:heart-list")
        context = {
            "object": heart,
            "type": "heart",
        }
        messages.error(request, "Failed to delete Heart data.")
        return render(request, "aida/generic/delete.html", context)
