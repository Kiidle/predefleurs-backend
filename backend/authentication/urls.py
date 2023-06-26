from django.urls import path
from . import views
from .views import SignUpView, HomeView, LegalNoticeView, PrivacyView, TermsView, AccountView, PersonalView, WorkView, \
    MetaView, AddressView, QualificationView, CertificateView, EducationView, HealthView, CriminalView, SalaryView, \
    AbsenceView, FeedbackView, ReprimantView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("", HomeView.as_view(), name="home"),
    path("legalnotice/", LegalNoticeView.as_view(), name="legalnotice"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
    path("terms/", TermsView.as_view(), name="terms"),
    path("settings/<int:pk>", AccountView.as_view(), name="settings"),
    path("settings/<int:pk>/personal", PersonalView.as_view(), name="settings_personal"),
    path("settings/<int:pk>/personal/meta", MetaView.as_view(), name="settings_meta"),
    path("settings/<int:pk>/personal/address", AddressView.as_view(), name="settings_address"),
    path("settings/<int:pk>/personal/qualification", QualificationView.as_view(), name="settings_qualification"),
    path("settings/<int:pk>/personal/qualification/certificates", CertificateView.as_view(),
         name="settings_certificate"),
    path("settings/<int:pk>/personal/qualification/educations", EducationView.as_view(), name="settings_education"),
    path("settings/<int:pk>/personal/health", HealthView.as_view(), name="settings_health"),
    path("settings/<int:pk>/personal/criminals", CriminalView.as_view(), name="settings_criminal"),
    path("settings/<int:pk>/work", WorkView.as_view(), name="settings_work"),
    path("settings/<int:pk>/work/salaries", SalaryView.as_view(), name="settings_salary"),
    path('salary/<int:salary_id>/', views.confirm_salary, name='salary_confirm'),
    path("settings/<int:pk>/work/absences", AbsenceView.as_view(), name="settings_absence"),
    path("settings/<int:pk>/work/feedback", FeedbackView.as_view(), name="settings_feedback"),
    path("settings/<int:pk>/work/reprimant", ReprimantView.as_view(), name="settings_reprimant"),
]
