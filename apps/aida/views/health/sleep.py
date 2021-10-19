from django.urls import reverse_lazy
from django.views import generic

from apps.aida.models.health.sleep import Sleep


# TODO: set permissions
class List(generic.ListView):
    model = Sleep
    context_object_name = "sleeps"
    queryset = Sleep.find_all()
    template_name = "aida/health/sleep/list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context["title"] = "Sleep Data"
        return context


class Create(generic.CreateView):
    model = Sleep
    context_object_name = "sleeps"
    queryset = Sleep.find_all()
    template_name = "aida/generic_form.html"
    fields = ("slept_at", "awoke_at")


class Detail(generic.DetailView):
    model = Sleep
    context_object_name = "sleep"
    template_name = "aida/health/sleep/detail.html"


class Update(generic.UpdateView):
    model = Sleep
    context_object_name = "sleep"
    template_name = "aida/generic_form.html"
    fields = ("slept_at", "awoke_at")


class Delete(generic.DeleteView):
    model = Sleep
    context_object_name = "sleep"
    template_name = "aida/generic_delete.html"
    success_url = reverse_lazy("aida:sleep-list")

    def get_context_data(self, **kwargs):
        context = super(Delete, self).get_context_data(**kwargs)
        context["type"] = "sleep"
        return context
