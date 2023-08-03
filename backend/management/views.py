from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from management.models import Task
from store.models import Reservation


# Create your views here.

class BoardView(generic.ListView):
    model = Task
    fields = ['title', 'description', 'priority', 'status', 'author', 'assigned']
    template_name = "pages/task/tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks_todo_emergency = Task.objects.filter(status=Task.Status.TODO, priority=Task.Priority.EMERGENCY)
        context["tasks_todo_emergency"] = tasks_todo_emergency
        tasks_todo_high = Task.objects.filter(status=Task.Status.TODO, priority=Task.Priority.HIGH)
        context["tasks_todo_high"] = tasks_todo_high
        tasks_todo_medium = Task.objects.filter(status=Task.Status.TODO, priority=Task.Priority.MEDIUM)
        context["tasks_todo_medium"] = tasks_todo_medium
        tasks_todo_low = Task.objects.filter(status=Task.Status.TODO, priority=Task.Priority.LOW)
        context["tasks_todo_low"] = tasks_todo_low

        tasks_inprogress_emergency = Task.objects.filter(status=Task.Status.IN_PROGRESS,
                                                         priority=Task.Priority.EMERGENCY)
        context["tasks_inprogress_emergency"] = tasks_inprogress_emergency
        tasks_inprogress_high = Task.objects.filter(status=Task.Status.IN_PROGRESS, priority=Task.Priority.HIGH)
        context["tasks_inprogress_high"] = tasks_inprogress_high
        tasks_inprogress_medium = Task.objects.filter(status=Task.Status.IN_PROGRESS, priority=Task.Priority.MEDIUM)
        context["tasks_inprogress_medium"] = tasks_inprogress_medium
        tasks_inprogress_low = Task.objects.filter(status=Task.Status.IN_PROGRESS, priority=Task.Priority.LOW)
        context["tasks_inprogress_low"] = tasks_inprogress_low

        tasks_done_emergency = Task.objects.filter(status=Task.Status.DONE,
                                                   priority=Task.Priority.EMERGENCY)
        context["tasks_done_emergency"] = tasks_done_emergency
        tasks_done_high = Task.objects.filter(status=Task.Status.DONE, priority=Task.Priority.HIGH)
        context["tasks_done_high"] = tasks_done_high
        tasks_done_medium = Task.objects.filter(status=Task.Status.DONE, priority=Task.Priority.MEDIUM)
        context["tasks_done_medium"] = tasks_done_medium
        tasks_done_low = Task.objects.filter(status=Task.Status.DONE, priority=Task.Priority.LOW)
        context["tasks_done_low"] = tasks_done_low

        context["tasks"] = super().get_queryset()

        return context


class CreateTaskView(generic.CreateView):
    model = Task
    fields = ['title', 'description', 'priority']
    template_name = "pages/task/form_task.html"

    def get_success_url(self):
        return reverse_lazy('board')

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class TaskView(generic.UpdateView):
    model = Task
    fields = ['title', 'description', 'priority', 'status', 'author', 'assigned']
    template_name = "pages/task/task.html"

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class UpdateTaskView(generic.UpdateView):
    model = Task
    fields = ['title', 'description', 'priority']
    template_name = "pages/task/form_task.html"

    def get_success_url(self):
        return reverse_lazy('task', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Aufgabe bearbeiten"

        return context


class AssignTaskView(generic.UpdateView):
    model = Task
    fields = ['assigned']
    template_name = "pages/task/form_task.html"

    def get_success_url(self):
        return reverse_lazy('task', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Aufgabe zuweisen"

        return context

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user != task.author:
            return HttpResponseRedirect(reverse_lazy('task', kwargs={'pk': task.pk}))
        return super().dispatch(request, *args, **kwargs)


class StatusTaskView(generic.UpdateView):
    model = Task
    fields = ['status']
    template_name = "pages/task/form_task.html"

    def get_success_url(self):
        return reverse_lazy('task', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Aufgabe aktualisieren"

        return context

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user != task.author and request.user != task.assigned:
            return HttpResponseRedirect(reverse_lazy('task', kwargs={'pk': task.pk}))
        return super().dispatch(request, *args, **kwargs)

class DeleteTaskView(generic.DetailView):
    model = Task
    fields = ['title']
    template_name = 'pages/task/delete_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("board")

    return (request, "/management", {"task": task})

class ManageReservationsView(generic.ListView):
    model = Reservation
    fields = ['article', 'start_date', 'status']
    template_name = "pages/reservations.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(Q(status=Reservation.Status.OPEN) | Q(status=Reservation.Status.APPROVED) | Q(status=Reservation.Status.READY))
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = self.get_queryset()
        return context

class ManageReservationsArchivedView(generic.ListView):
    model = Reservation
    fields = ['article', 'start_date', 'status']
    template_name = "pages/reservation_archived.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(Q(status=Reservation.Status.DENIED) | Q(status=Reservation.Status.DONE))
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = self.get_queryset()
        return context

class UpdateReservation(generic.UpdateView):
    model = Reservation
    fields = ['status']
    template_name = "pages/form_reservation.html"

    def get_success_url(self):
        return reverse_lazy('manage_reservations')

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

