from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from management.models import Task
from store.models import Reservation

User = get_user_model()



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

class ManageUsersView(generic.ListView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = "pages/users/users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = self.get_queryset()
        context["users_admin"] = self.get_queryset().filter(groups__name='admin')
        context["users_developer"] = self.get_queryset().filter(groups__name='developer')
        context["users_staff"] = self.get_queryset().filter(groups__name='staff')
        context["users_customer"] = self.get_queryset().filter(groups__name='customer')
        return context

class ManageUserView(generic.DetailView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = "pages/users/user.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        username = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset.filter(username=username)
        obj = get_object_or_404(queryset)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ChangeUsergroupView(generic.UpdateView):
    template_name = 'pages/users/update_role.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        groups = Group.objects.all()
        context = {'user': user, 'groups': groups}
        return render(request, self.template_name, context)

    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        group_id = request.POST.get('group')
        if group_id:
            group = get_object_or_404(Group, id=group_id)
            user.groups.clear()  # Clear existing groups
            user.groups.add(group)
            messages.success(request, f'Group for {user.username} has been updated.')
            return redirect('manage_user', username=user.username)
        return redirect('manage_user', username=user.username)


class ManageUserPersonalMetaView(generic.DetailView):
    model = User
    template_name = "pages/users/personal/meta.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        username = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset.filter(username=username)
        obj = get_object_or_404(queryset)
        return obj

class ManageUserPersonalMetaUpdateView(generic.UpdateView):
    model = User
    fields = ['username']
    template_name = "pages/users/personal/form_meta.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        username = self.kwargs.get(self.slug_url_kwarg)
        queryset = queryset.filter(username=username)
        obj = get_object_or_404(queryset)
        return obj