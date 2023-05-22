from django.urls import path
from . import views
from .views import SignUpView, HomeView, LegalNoticeView, PrivacyView, TermsView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("", HomeView.as_view(), name="home"),
    path("legalnotice", LegalNoticeView.as_view(), name="legalnotice"),
    path("privacy", PrivacyView.as_view(), name="privacy"),
    path("terms", TermsView.as_view(), name="terms"),
]