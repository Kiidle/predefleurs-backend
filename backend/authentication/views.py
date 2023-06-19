from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import Group
from .models import Data, Address, Personal

from django.db.models.signals import post_save

from .forms import SignUpForm, LoginForm

from django.contrib.auth import authenticate, get_user_model, login, logout
User = get_user_model()



# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "pages/authentication/signup.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='customer')
        group, created = Group.objects.get_or_create(name='staff')
        group, created = Group.objects.get_or_create(name='developer')
        group, created = Group.objects.get_or_create(name='admin')

    def form_valid(self, form):
        response = super().form_valid(form)
        group = Group.objects.get(name='customer')
        self.object.groups.add(group)
        return response

    @receiver(post_save, sender=User)
    def create_user_settings(sender, instance, created, **kwargs):
        if created:
            Data.objects.create(user=instance)
            Personal.objects.create(user=instance)
            Address.objects.create(user=instance)

def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        form = LoginForm()
        return render(request, "pages/authentication/login.html", {"form": form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Erfolgreich angemeldet!")
                return redirect("home")

        messages.error(request, f"Benutzername oder Passwort ist falsch.")
        return render(request, "pages/authentication/login.html", {"form": form})

@login_required
def custom_logout(request):
    logout(request)
    return redirect("home")


class HomeView(generic.ListView):
    model = User
    template_name = "pages/root/home.html"

class LegalNoticeView(generic.ListView):
    model = User
    template_name = "pages/laws/legalnotice.html"

class PrivacyView(generic.ListView):
    model = User
    template_name = "pages/laws/privacy.html"

class TermsView(generic.ListView):
    model = User
    template_name = "pages/laws/terms.html"


class AccountView(generic.UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/account.html"

    def get_success_url(self):
        return reverse_lazy('settings', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        return super().form_valid(form)


class PersonalView(generic.ListView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/personal/personal.html"

class MetaView(generic.DetailView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/personal/meta.html"

class AddressView(generic.DetailView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/personal/address.html"

class QualificationView(generic.DetailView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/personal/qualification/qualification.html"

class WorkView(generic.ListView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/work/work.html"

class CertificateView(generic.DetailView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/personal/qualification/certificate.html"

class EducationView(generic.DetailView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/personal/qualification/education.html"

class HealthView(generic.DetailView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/personal/health.html"

class CriminalView(generic.DetailView):
    model = User
    fields = ['username', 'email']
    template_name = "pages/settings/personal/criminal.html"