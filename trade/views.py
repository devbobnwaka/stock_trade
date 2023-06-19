from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Trade
from .permissions import RedirectHomeIfLogInMixin



# Create your views here.
class Login(RedirectHomeIfLogInMixin, LoginView):
    template_name = "accounts/login.html"


class Dashboard(LoginRequiredMixin, View):

    def get(self, request):
        # <view logic>
        if self.request.user.is_admin:
            return render(request, 'trade/admin_dashboard.html', {})  # Use the template for admin template
        else:
            return render(request, 'trade/user_dashboard.html', {}) # Use the template for not admin users 



class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')
